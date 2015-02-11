import sys
#sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
from voucr.views import signup, login, index, logout

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^signup/$', signup),
)
