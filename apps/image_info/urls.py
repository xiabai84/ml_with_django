# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

"""PyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
# from stock_info import views
from .views import UploadImageView
# from ml_with_django.settings import BASE_DIR

import os

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
global_file_path = os.path.join(app_path, 'static')

urlpatterns = [
    url(r'^upload_image/', UploadImageView.as_view(), name="upload image"),
]
