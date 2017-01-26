from django.conf.urls import url
from booksearch import views

urlpatterns = [
    url(r'^$', views.search_form, name='search-form'),
    url(r'^searchform/$', views.start_search, name='start-search'),
]