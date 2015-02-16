from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    longname = models.CharField(max_length=255)
    username_url = models.CharField(max_length=20, db_index=True)

class UserInfoForm(ModelForm):
    class meta:
        model = UserInfo
        field = ['longname','username_url']

class Campaign(models.Model):
    user = models.ForeignKey(UserInfo)
    desc_url = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

class CampaignForm(ModelForm):
    class meta:
        model = Campaign
        field = ['desc_url','desc', 'count']
        

class Voucher(models.Model):
    campaign = models.ForeignKey(Campaign)
    char_url = models.CharField(max_length=20, db_index=True)
    word_url = models.CharField(max_length=20, db_index=True)
    date_url = models.CharField(max_length=7, db_index=True)
    expire_date = models.DateField()
    
class VoucherForm(ModelForm):
    class meta:
        model = Voucher
        field = ['char_url','word_url','expire_date']    
    
