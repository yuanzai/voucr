import sys
#sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
from voucr.views import signup_page, login_page, index, logout_page

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^login/$', login_page),
    url(r'^logout/$', logout_page),
    url(r'^signup/$', signup_page),
)
