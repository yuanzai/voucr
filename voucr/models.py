from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm

import pytz
from timezone_field import TimeZoneField

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    company_name = models.CharField(max_length=255)
    company_short_url = models.CharField(max_length=20, db_index=True)
    address_1 = models.CharField(max_length=255, default='')
    address_2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, default='')
    timezone = TimeZoneField(default='')


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        field = ['company_name','username_url']
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        for key, f in self.fields.iteritems():
            f.widget.attrs.update({'class':'form-control'})

class Campaign(models.Model):
    offer_choices = (
		    ('Free','Free'),
		    ('BuyNGet','Free With Purchase'),
		    ('Disc','Discount'))
    distribution_choices = (
    	               ('Public','Public - Anyone can enter email/mobile no.'),
    	               ('User','User - Only a logged in user can enter an email/mobile no.'),
    	               ('None','None - All voucher codes are populated without distribution'))
    delivery_choices = (
    	               ('Email','Email only'),
    	               ('Mobile','Mobile only'),
    	               ('Email & Mobile','Email and mobile'))
    	               
    user = models.ForeignKey(User)
    desc_url = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255, null=True)
    offer_type = models.CharField(max_length=30,
		                 choices=offer_choices,
				 default='Free')
    distribution = models.CharField(max_length=30,
		                   choices=distribution_choices,
				   default='None')
    delivery = models.CharField(max_length=30,
		               choices=delivery_choices,
			       default='Email')
    count = models.PositiveIntegerField()
    expire_datetime = models.DateTimeField(null=True)

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        #field = ['desc_url','desc', 'count','expire_date']
        exclude = ('user',)        

class Voucher(models.Model):
    campaign = models.ForeignKey(Campaign)
    char_url = models.CharField(max_length=20, db_index=True)
    word_url = models.CharField(max_length=20, db_index=True)
    date_url = models.CharField(max_length=7, db_index=True)
    delivery_destination = models.CharField(max_length=255, null=True)
    expire_datetime = models.DateTimeField(null=True)
    claim_datetime = models.DateTimeField(null=True)
    is_claimed = models.BooleanField(default=False)

