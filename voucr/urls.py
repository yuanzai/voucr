import sys
#sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
#from voucr.views import signup_page, login_page, index, logout_page, get_voucher
import voucr.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index),
    url(r'^login$', views.login_page),
    url(r'^logout$', views.logout_page),
    url(r'^signup$', views.signup_page),
    url(r'^(?P<char_url>\s+)$', views.get_voucher),
    url(r'^(?P<username_url>\s+)$', views.user_home),
    url(r'^(?P<username_url>\s+)/create$', views.user_create),
)
