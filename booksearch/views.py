# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from booksearch.forms import SearchForm
from booksearch.models import Page
from django.conf import settings
from django.template.loader import render_to_string
from time import time
from datetime import datetime
from decorator import decorator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Booksearch.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

@decorator
def timer(func, *args, **kwargs):
    """Decorator for receivig function returning time """
    t_before = time()
    func(*args, **kwargs)
    t_after = time()
    dt = t_after - t_before;
    return func(*args, **kwargs), dt

def search_form(request):
    form = SearchForm()
    context = {
        "form": form,
        "time": time
    }
    return render(request, 'booksearch/search_form.html', context)

@timer
def searchFunc(text):
    try:
        result = Page.objects.filter(text__search=text)
    except Exception:
        return None
    return result

@login_required
def start_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, instance=request.user)
        if form.is_valid():
            searchText = unicode(form.cleaned_data['searchText'])
            email = form.cleaned_data['email']

            result, searchTime =searchFunc(searchText)

            logger.info("{} : Search request for word '{}' takes {} sec".format(datetime.now(), searchText, searchTime))

            emailContext = {
                "result": result,
                "text" : searchText,
                "user" : request.user,
            }

            body = render_to_string('booksearch/email_tmpl.html', emailContext)

            if body:
                try:
                    send_mail(settings.EMAIL_SUBJECT, body, settings.EMAIL_HOST_USER, [email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                context = {
                    'word': searchText,
                    'email': email,
                }
                return render(request, 'booksearch/search_start.html', context)
            else:
                form = SearchForm()
                context = {"form": form}
                return render(request, 'booksearch/search_form.html', context)
