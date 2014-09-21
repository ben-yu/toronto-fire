from django.conf.urls import patterns, include, url
from django.contrib import admin

from toronto_fire.views import IncidentsView

urlpatterns = patterns('',
    url(r'^$', IncidentsView.as_view(), name='incidents-view'),
    url(r'^admin/', include(admin.site.urls)),
)
