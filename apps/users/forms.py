# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django import forms


class LoginForm(forms.Form):
    '''
    username and password is identified by login.html see form
    '''
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
