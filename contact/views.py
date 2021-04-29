from django.shortcuts import render
from about.models import AboutTheCompany, ContactInfo, social_link

def contact_page(request):    
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    template_name = 'contact.html'
    context ={
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    return render(request, template_name,context)