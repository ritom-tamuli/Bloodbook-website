from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    #additional
    state = models.CharField(max_length=264,blank=False)
    city = models.CharField(max_length=264,blank=False)
    phno = models.CharField(max_length=128,blank=False)
    BloodGroup = models.CharField(max_length=128,blank=False)
    def __str__(self):
        return self.user.username
