# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class SearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['searchText'] = forms.CharField(required=True, max_length=100)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta():
        model = User
        fields = ('email', )
