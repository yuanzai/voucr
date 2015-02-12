from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=true)
    longname = models.CharField(max_length=255)
    urlshortname = models.CharField(max_length=20, db_index=true)

class Campaign(models.Model)
    user = models.ForeignKey(UserInfo)
    desc_url = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)

class Voucher(models.Model)
    campaign = models.ForeignKey(Campaign)
    char_url = models.CharField(max_length=20, db_index=true)
    word_url = models.CharField(max_length=20, db_index=true)
    date_url = models.CharField(max_length=7, db_index=true)
    expire_date = models.DateField()
    
    
    
