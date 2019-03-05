# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View

from .models import UserProfile
from .forms import LoginForm


class CustomBackend(ModelBackend):
    '''
    custom authentication by using username and email in combination with django user admin module
    for setting.py -> AUTHENTICATION_BACKENDS
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # get must be return only one obj
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    '''
    login class for login.html
    '''
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)    # verify post input via forms.LoginForm
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                login(request, user)    # finished user login!
                return redirect("/image_info/upload_image")
            else:
                return render(request, "login.html", {"msg": "username or password is false"})
        else:
            return render(request, "login.html", {"login_form": login_form})


def user_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect("/login/")


def page_not_found(request):
    # global 404 error
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # global 500 error
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
