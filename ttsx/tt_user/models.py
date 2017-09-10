from django.db import models

# Create your models here.
class UserInfoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isValid=True)
    def create_user (self,uname,upwd,uemail):
        user_info=UserInfo()
        user_info.uname=uname
        user_info.upwd=upwd
        user_info.uemail=uemail
        return user_info

class UserInfo (models.Model):
    uname= models.CharField(max_length=20)
    upwd= models.CharField(max_length=20)
    uemail= models.CharField(max_length=30)
    isValid = models.BooleanField(default=True)
    isActive=models.BooleanField(default=False)
    users=UserInfoManager()


class UserAddressInfo (models.Model):
     uname=models.CharField(max_length=20)
     uaddress=models.CharField(max_length=100)
     uphone=models.CharField(max_length=11)
     user=models.ForeignKey('UserInfo')

