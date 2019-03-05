# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

import xadmin
from xadmin import views


class BaseSetting(object):
    '''
    enable themes in xadmin navi-bar on top-right by using bootstrap
    :var enable_themes; use_bootstswach
    '''
    enable_themes = False
    use_bootswatch = True


class GlobalSettings(object):
    '''
    setting title in navi-bar on top-left and footer
    '''
    site_title = "Admin Board"
    site_footer = "Bai Xia, Munich"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
