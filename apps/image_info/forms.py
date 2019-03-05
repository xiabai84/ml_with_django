# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django import forms


class PostForm(forms.Form):
    image = forms.ImageField()
