from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class intro(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class homeservices(models.Model):
    logo = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class feature(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    logo = models.ImageField(upload_to='media')
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.title
