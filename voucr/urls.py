import sys
sys.path.append('/home/ec2-user/voucr')

from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voucr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login/template/login.html'}),
)
