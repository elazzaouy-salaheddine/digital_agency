from django.shortcuts import render
from .models import service
from about.models import AboutTheCompany, ContactInfo, social_link
# Create your views here.


def services_page(request):
    services = service.objects.all()
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    template_name = 'services.html'
    context ={
        'services':services,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    return render(request, template_name,context)