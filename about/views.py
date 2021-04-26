from django.shortcuts import render
from .models import about_us, numbers, skills, testimonial
# Create your views here.


def about_page(request):
    about = about_us.objects.all()
    number = numbers.objects.all()
    skill = skills.objects.all()
    testimonials = testimonial.objects.all()
    template_name = 'about.html'
    context ={
        'about':about,
        'numbers':number,
        'skills':skill,
        'testimonials':testimonials
    }
    return render(request, template_name,context)