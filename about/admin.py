from django.contrib import admin
from .models import about_us,numbers,skills,testimonial,AboutTheCompany,ContactInfo,social_link,Terms_of_service,Privacy_policy
# Register your models here.
admin.site.register(AboutTheCompany)
admin.site.register(about_us)
admin.site.register(numbers)
admin.site.register(skills)
admin.site.register(testimonial)
admin.site.register(ContactInfo)
admin.site.register(social_link)
admin.site.register(Terms_of_service)
admin.site.register(Privacy_policy)