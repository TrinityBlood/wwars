from django.conf.urls import patterns, url

from api.views import SituationView

urlpatterns = patterns('',
    url(r'^situation/$', SituationView.as_view(), name='api:situation'),
)
