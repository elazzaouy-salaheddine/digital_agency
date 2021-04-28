from django.contrib import admin
from .models import about_us,numbers,skills,testimonial,about_the_company,ContactInfo,social_link
# Register your models here.
admin.site.register(about_the_company)
admin.site.register(about_us)
admin.site.register(numbers)
admin.site.register(skills)
admin.site.register(testimonial)
admin.site.register(ContactInfo)
admin.site.register(social_link)