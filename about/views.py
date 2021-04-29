from django.shortcuts import render
from .models import about_us, numbers, skills, testimonial,AboutTheCompany, ContactInfo, social_link,Privacy_policy,Terms_of_service
# Create your views here.


def about_page(request):
    about = about_us.objects.all()
    number = numbers.objects.all()
    skill = skills.objects.all()

    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    testimonials = testimonial.objects.all()
    template_name = 'about.html'
    context ={
        'about':about,
        'numbers':number,
        'skills':skill,
        'testimonials':testimonials,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    return render(request, template_name,context)

def privacy_policy(request):
    Privacy_polic = Privacy_policy.objects.first()
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    testimonials = testimonial.objects.all()
    template_name = 'privacy_policy.html'
    context ={

        'testimonials':testimonials,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links,
        'Privacy_policy':Privacy_polic
    }
    return render(request, template_name,context)

def terms_of_service(request):
    Terms_of_services = Terms_of_service.objects.first()
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    testimonials = testimonial.objects.all()
    template_name = 'terms_of_service.html'
    context ={

        'testimonials':testimonials,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links,
        'Terms_of_services':Terms_of_services
    }
    return render(request, template_name,context)