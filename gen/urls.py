# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from gen.views import *

urlpatterns = [
    url(r'^body/$', body),
    url(r'^proc/$', proc),
    url(r'^text/$', text),
]