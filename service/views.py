from django.shortcuts import render
from .models import service
# Create your views here.


def services_page(request):
    services = service.objects.all()
    template_name = 'services.html'
    context ={
        'services':services
    }
    return render(request, template_name,context)