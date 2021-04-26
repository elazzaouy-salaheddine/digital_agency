from django.shortcuts import render

# Create your views here.


def contact_page(request):
    template_name = 'contact.html'
    return render(request, template_name)