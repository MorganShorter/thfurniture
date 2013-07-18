# -*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf.urls.defaults import *
from django.conf import settings
from satchmo_store.urls import urlpatterns

urlpatterns += patterns('',
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '%sfavicon.ico' % settings.STATIC_URL}),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    #url(r'^paysbuyresp/$', 'payment.modules.paysbuy.views.tester'),
)
