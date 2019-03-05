# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

import xadmin
from .models import CustomerImage


class ImageInfoAdmin(object):

    list_display = ['username', 'img_name', 'upload_time', 'recording', 'damage_grad', 'is_right_estimation', 'cust_img_url', 'ml_img_url']
    search_fields = ['username', 'img_name', 'upload_time', 'recording', 'damage_grad', 'is_right_estimation', 'cust_img_url', 'ml_img_url']
    list_filter = ['username', 'img_name', 'upload_time', 'recording', 'damage_grad', 'is_right_estimation']
    list_editable = ['img_name', 'is_right_estimation', 'recording']
    # import_excel = True
    #
    # def post(self, request, *args, **kwargs):
    #     if 'excel' in request.FILES:
    #         pass
    #     return super(ImageInfoAdmin, self).post(request, args, kwargs)


xadmin.site.register(CustomerImage, ImageInfoAdmin)
