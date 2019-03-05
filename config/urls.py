# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.views.static import serve
import xadmin

from users.views import LoginView, user_logout

from config.settings.local import STATIC_ROOT

import os

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
global_file_path = os.path.join(app_path, 'static')

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),  # serve is only used for dev not for prod!!!
    url(r'^$', TemplateView.as_view(template_name="login.html"), name="start_page"),
    url(r'^base/$', TemplateView.as_view(template_name="base_.html"), name="base_page"),
    url(r'^admin/', xadmin.site.urls),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', user_logout),
    url(r'^image_info/', include("image_info.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
