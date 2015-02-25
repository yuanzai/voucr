import sys
#sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from voucr.views import campaign_create, user_home, user_create, signup_page, login_page, index, logout_page, get_voucher, get_voucher_word
import voucr.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    #url(r'^login$', login_page),
    #url(r'^logout$', logout_page),
    url(r'^login?//$', auth_views.login, {'template_name': 'login.html'},name='login'),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    
    url(r'^signup/$', voucr.views.signup_page),
    url(r'^signup$', voucr.views.signup_page),
    
    url(r'^user_create/$', voucr.views.user_create),
    url(r'^campaign_create$', voucr.views.campaign_create),
    url(r'^campaign$', voucr.views.campaign_home),
    
    url(r'^campaign/(?P<campaign_id>\d+)$', voucr.views.campaign_view),
    #url(r'^(?P<username_url>\s+)/$', user_home),
    
    #**** Voucher ****
    url(r'^claim$', voucr.views.voucher_claim),
    url(r'^(?P<char_url>\w+)$', get_voucher),
    #url(r'^(?P<username_url>\w+)\(?P<word_url>\w+)$', get_voucher_word),
)
