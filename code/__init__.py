# -*- coding: utf-8 -*-






def classFactory(iface):


    from .pyarchinitPlugin import PyArchInitPlugin
    return PyArchInitPlugin(iface)
