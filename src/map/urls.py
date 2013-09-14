from django.conf.urls import patterns, url

from map.views import MapIndexView

urlpatterns = patterns('',
    url(r'^$', MapIndexView.as_view(), name='map:index'),
)
