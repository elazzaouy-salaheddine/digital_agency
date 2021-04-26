from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class portfolio_item(models.Model):
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    client = models.CharField(max_length=255)
    project_date = models.DateField(null=False,blank=False)
    project_url = models.URLField()
    project_detail = RichTextField()
    logo = models.ImageField(upload_to='media/portfolio')

    def __str__(self):
        return self.client
