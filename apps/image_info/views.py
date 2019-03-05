# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

import os
from django.shortcuts import render, redirect
from django.views.generic import View
import datetime

from .models import CustomerImage
from .util import get_classification_single, get_dmg_classification_single


class UploadImageView(View):

    def get(self, request):

        if request.user.is_authenticated:
            # return all images from the use, who sends this request
            usr_img = CustomerImage.objects.all().filter(username=request.user)
            return render(request, "predict_image.html", {'usr_img': usr_img})
        else:
            return render(request, "login.html", {"msg": "You should login first!"})

    def post(self, request):

        if request.user.is_authenticated:
            username = request.user.username
            user_id = request.user.id
            upload_file_list= request.FILES.getlist('upload_files')
            upload_timestamp = datetime.datetime.now()
            is_original = True
            # pre calculated for file/dir name
            d = datetime.date.today()
            year = '{:04d}'.format(d.year)
            month = '{:02d}'.format(d.month)
            day = '{:02d}'.format(d.day)
            today= year+"_"+month+"_"+day+"_"
            # find program root dir based on the position of this image_info/view.py
            root_path = os.path.dirname(os.path.abspath(__file__)).replace('/apps', '').replace('/image_info', '')

            for file in upload_file_list:
                # change filename by storing in fs
                file.name = str(user_id)+ "_" + today + file.name

                # calculate current month for generating dir for images
                curr = year + month + "/"

                # prepare media dir for storing upload and estimated images
                cust_img_url = root_path + '/media/cust_upload/' + curr + file.name

                # first estimation
                three_class_result = get_classification_single(file)
                # calculate dmg_result and return a estimated image
                dmg_result, grad_file = get_dmg_classification_single(file, three_class_result, str(user_id), upload_timestamp)
                ml_img_url = root_path + '/media/' + grad_file
                # ml_img_url = root_path + '/media/ml_estimated/' + curr + file.name

                # save new record in database see CustomerImage model
                CustomerImage.objects.create(img_name=file.name, username=username, upload_time=upload_timestamp,
                                             is_right_estimation=is_original, recording=three_class_result,
                                             damage_grad=dmg_result, img_file=file, pred_file=grad_file,
                                             cust_img_url=cust_img_url, ml_img_url=ml_img_url)

            return redirect("/image_info/upload_image")
        else:
            # if user try to use this ml-model without login...
            return render(request, "login.html", {"msg": "You should login first!"})
