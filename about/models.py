from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class ContactInfo(models.Model):
    address = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    zip_code = models.CharField(max_length=255,null=True,blank=True)
    contry = models.CharField(max_length=255,null=True,blank=True)
    phone_number_01 = models.CharField(max_length=255,null=True,blank=True)
    phone_number_02 = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=254)


class AboutTheCompany(models.Model):
    body = models.TextField()

class social_link(models.Model):
    link = models.URLField()
    social_name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255,default='facebook')

    def __str__(self):
        return self.social_name

class about_us(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    logo = models.ImageField(upload_to='media')

class numbers(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class skills(models.Model):
    name = models.CharField(max_length=255)
    num = models.FloatField()
    progressbar_color = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class testimonial(models.Model):
    image = models.ImageField(upload_to='media/tetstimonial')
    fulle_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    testimonial_item = models.TextField()

    def __str__(self):
        return self.fulle_name

class Terms_of_service(models.Model):
    body = models.TextField()

class Privacy_policy(models.Model):
    body = models.TextField()