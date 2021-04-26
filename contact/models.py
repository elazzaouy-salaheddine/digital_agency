from django.db import models

# Create your models here.


class contact(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    contry = models.CharField(max_length=255)
    phone_01 = models.CharField(max_length=255)
    phone_02 = models.CharField(max_length=255,null=False,blank=False)
    email_01 = models.CharField(max_length=255)
    email_02 = models.CharField(max_length=255,null=False,blank=False)