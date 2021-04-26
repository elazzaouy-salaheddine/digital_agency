from django.shortcuts import render
from .models import intro, homeservices, feature
# Create your views here.


def home_page(request):
    into = intro.objects.all()
    homeservice = homeservices.objects.all()
    industries = feature.objects.all()
    template_name = 'home.html'
    context = {
        'intor':into,
        'homeservices':homeservice,
        'industries':industries
    }
    return render(request, template_name, context)