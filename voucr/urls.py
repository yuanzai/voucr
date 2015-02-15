import sys
#sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
from voucr.views import user_home, user_create, signup_page, login_page, index, logout_page, get_voucher
#import voucr.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^login$', login_page),
    url(r'^logout$', logout_page),
    url(r'^signup/$', signup_page),
    url(r'^signup$', signup_page),
    url(r'^(?P<char_url>\s+)$', get_voucher),
    url(r'^(?P<username_url>\s+)$', user_home),
    url(r'^(?P<username_url>\s+)/create$', user_create),
)
