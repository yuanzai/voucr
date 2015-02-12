from django.db import models

class UserInfo(models.Model):
    shortname = models.CharField(max_length=20, db_index=true)
    user = models.OneToOneField(User, primary_key=true)
    longname = models.CharField(max_length=255)


class Campagin(modes
