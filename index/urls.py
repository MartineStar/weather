from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^getdata/$', dataViews),
    url(r'^voice/$', voiceViews),
    url(r'^login/$', loginViews, name='log'),
    url(r'^register/$', registerViews, name='reg'),
    url(r'^message/$', feedbackViews),
    url(r'^$', indexViews),
]
