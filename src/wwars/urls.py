from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from wwars.views import IndexView, ThreadView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwars.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^map/', include('map.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thread/(?P<thread_id>\d+)/$', ThreadView.as_view(), name='thread_view'),
)

