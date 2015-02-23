from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    longname = models.CharField(max_length=255)
    username_url = models.CharField(max_length=20, db_index=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        field = ['longname','username_url']
        exclude = ('user',)

class Campaign(models.Model):
    offer_choices = (
		    ('Free','Free'),
		    ('BuyNGet','Free With Purchase'),
		    ('Disc','Discount'))
	
    user = models.ForeignKey(User)
    desc_url = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255, null=True)
    offer_type = models.CharField(max_length=30,
		                 choices=offer_choices,
				 default='Free')
    count = models.PositiveIntegerField()
    expire_date = models.DateField(null=True)

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        field = ['desc_url','desc', 'count','expire_date']
        exclude = ('user',)        

class Voucher(models.Model):
    campaign = models.ForeignKey(Campaign)
    char_url = models.CharField(max_length=20, db_index=True)
    word_url = models.CharField(max_length=20, db_index=True)
    date_url = models.CharField(max_length=7, db_index=True)
    expire_date = models.DateField(null=True)
    claim_datetime = models.DateTimeField(null=True)
    is_claimed = models.BooleanField(default=False)

