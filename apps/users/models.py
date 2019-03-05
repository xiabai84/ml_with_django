# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    '''
    this model simplify user management module and user login by using django admin
    '''
    nick_name = models.CharField(max_length=50, verbose_name="Nickname", default="")
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="Gender", choices=(("male", "male"), ("female", "female")), default="female",
                              max_length=6)
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
