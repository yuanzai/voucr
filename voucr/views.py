from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


from models import UserCreateForm, UserInfo, UserInfoForm, Campaign, CampaignForm, Voucher
import sys
from link_gen import link_generator
from datetime import datetime

def check_user_info(user):
    ui = UserInfo.objects.filter(user=user)
    if ui.count() != 1:
        return False
    else:
        return True

def index(request):
    if not request.user.is_authenticated():
        return render(request,'index.html')
    else:
        ui = UserInfo.objects.filter(user=request.user)
        if ui.count() != 1:
	        return HttpResponseRedirect(reverse('voucr.views.user_create'))
        else:
    	    c = Campaign.objects.filter(user=request.user)
            u = ui[0]
            return render(request, 'campaign_home.html', {'c' : c, 'u' : u })
    	
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('voucr.views.index'))

def login_page(request):
    if request.method == 'POST':
    	form = AuthenticationForm(request.POST)
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(username=username, password=password)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse("OK")
            return HttpResponseRedirect(reverse('voucr.views.index'))
        else:
            return HttpResponse("not OK")
            #return render(request, 'login.html',{'form':form})
        """
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('voucr.views.index'))
            else:
            	# Return a 'disabled account' error message
                return HttpResponse('Account disabled, please contact us.')
        else:
            
            form.fields['username'].widget.attrs.update({'class':'form-control'})
            form.fields['password'].widget.attrs.update({'class':'form-control'})
            return render(request, 'login.html',{'form':form})
        """
    else:
        form = AuthenticationForm()
        
    form.fields['username'].widget.attrs.update({'class':'form-control'})
    form.fields['password'].widget.attrs.update({'class':'form-control'})
    return render(request, 'login.html',{'form':form})

def signup_page(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            form = authenticate(username=username,
                                password=password)
            login(request, form)
            return HttpResponseRedirect(reverse('voucr.views.user_create'))
        return render(request, 'signup.html',{'form':form})
    else:
        form = UserCreateForm()
        return render(request, 'signup.html',{'form':form})

def get_voucher(request, char_url):
    v = Voucher.objects.filter(char_url=char_url).filter(is_claimed=False)
    if v.count() != 1:
        raise Http404("Poll does not exist")
    else:
        v = v[0]
        c = v.campaign
        u = UserInfo.objects.get(user=c.user)
        return render(request, 'voucher.html', {'c': c, 'u' : u, 'v' : v })

def get_voucher_word(request, username_url, word_url):
    c = Campaign.objects.get(username_url=username_url)
    v = Voucher.objects.filter(campaign=c).filter(word_url=word_url)
    if v.count() != 1:
        return render(request, 'no_voucher.html')
    else:
        u = UserInfo.objects.get(user=c.user)
        return render(request, 'voucher.html', {'c': c, 'u': u, 'v' : v})

def voucher_claim(request):
    if request.method == 'POST':
        v = Voucher.objects.get(char_url=request.POST['char_url'])
        v.claim_datetime = datetime.now()
        v.is_claimed = True
        v.save()
        c = v.campaign
        u = UserInfo.objects.get(user=c.user)
        return render(request, 'voucher_claim.html', {'c': c, 'u' : u})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def user_create(request):
    #if not request.user.is_authenticated():
        #return HttpResponseRedirect(reverse('voucr.views.index'))
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
    	    return HttpResponse('user info saved')
        return render(request, 'user_create.html',{'form':form})
    else:
    	form = UserInfoForm()
    	item = UserInfo.objects.filter(user=request.user)
    	newuser = True
        if item.count() == 1:
    	    form = UserInfoForm(instance=item[0])
            newuser = False
        return render(request, 'user_create.html',{'form':form, 'newuser' : newuser})

def campaign_home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('voucr.views.index'))
    if not check_user_info(request.user):
	    return HttpResponseRedirect(reverse('voucr.views.user_create'))
    c = Campaign.objects.filter(user=request.user)
    return render(request, 'campaign_home.html', {'c' : c })

def campaign_view(request, campaign_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if not check_user_info(request.user):
	    return HttpResponseRedirect(reverse('voucr.views.user_create'))
    c = Campaign.objects.get(id=campaign_id)
    v = Voucher.objects.filter(campaign=c)
    return render(request, 'campaign_view.html', {'c': c, 'v' : v})


def campaign_create(request): 
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('voucr.views.index'))
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            link_generator(newform)            
            return HttpResponse('campaign saved')
        return render(request, 'campaign_create.html',{'form':form})
    else:
        form = CampaignForm()
        return render(request, 'campaign_create.html',{'form':form})

def user_home(request):
    return HttpResponse('voucher')
