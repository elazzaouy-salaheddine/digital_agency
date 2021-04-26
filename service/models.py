from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class service(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    ng_image = models.ImageField(upload_to='media/service')

    def __str__(self):
        return self.title
