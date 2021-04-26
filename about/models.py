from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class about_the_company(models.Model):
    body = models.TextField()


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