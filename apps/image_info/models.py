# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class CustomerImage(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="id (primary key)")
    username = models.CharField(max_length=64, verbose_name="username")
    img_name = models.CharField(max_length=64, verbose_name="image name")
    upload_time = models.DateTimeField(verbose_name='upload timestamp')
    is_right_estimation = models.BooleanField(default=True, verbose_name='verified result')
    recording = models.CharField(max_length=64, verbose_name="type of recording")
    damage_grad = models.CharField(max_length=64, verbose_name="damage grade")
    img_file = models.ImageField(upload_to="cust_upload/%Y%m", verbose_name="original image", blank=True)
    pred_file = models.ImageField(upload_to="ml_estimated/%Y%m", verbose_name="estimated image", blank=True)
    cust_img_url = models.CharField(max_length=256, verbose_name="customer upload path")
    ml_img_url = models.CharField(max_length=256, verbose_name="estimated image path")

    class Meta:
        verbose_name = "customer image"
        verbose_name_plural = verbose_name


@receiver(pre_delete, sender=CustomerImage)
def model_delete(sender, instance, **kwargs):
    '''
    if you are using default django ImageField model. The image file won't be removed from disk via django-admin-delete,
    because model only stores meta information of the image. In order to delete the file from disk it is necessary to
    implement a customized delete function by using "receive pre_delete or post_delete" see code below.

    Delete will remove local file by passing False to FileField/ImageField instance
    Link: https://stackoverflow.com/questions/13857007/using-pre-delete-signal-in-django
    '''
    instance.img_file.delete(False)
    instance.pred_file.delete(False)
