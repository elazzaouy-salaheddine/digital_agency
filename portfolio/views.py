from django.http import Http404
from django.shortcuts import render
from .models import portfolio_item, category
from about.models import AboutTheCompany, ContactInfo, social_link


# Create your views here.

def portfolio_page(request):
    portfolio_items = portfolio_item.objects.all()
    categorys = category.objects.all()

    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    template_name = 'portfolio.html'
    context = {
        'portfolio_items':portfolio_items,
        'categorys':categorys,
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    return render(request, template_name, context)


def portfolio_detail(request,id):
    AboutTheCompan = AboutTheCompany.objects.first()
    ContactInf = ContactInfo.objects.first()
    social_links = social_link.objects.all()
    context = {
        'AboutTheCompany':AboutTheCompan,
        'ContactInfo':ContactInf,
        'social_link':social_links
    }
    try:
        portfolio_items = portfolio_item.objects.get(id=id)
    except portfolio_item.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'portfolio_detail.html',context)