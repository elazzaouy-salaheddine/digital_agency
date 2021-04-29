from django.shortcuts import render
from about.models import AboutTheCompany, ContactInfo, social_link
from .models import intro, homeservices, feature

# Create your views here.

def home_page(request):
    into = intro.objects.all()
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    homeservice = homeservices.objects.all()
    industries = feature.objects.all()
    template_name = 'home.html'
    context = {
        'intor':into,
        'homeservices':homeservice,
        'industries':industries,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    return render(request, template_name, context)