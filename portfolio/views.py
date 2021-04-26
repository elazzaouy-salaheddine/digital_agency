from django.shortcuts import render
from .models import portfolio_item
# Create your views here.


def portfolio_page(request):
    portfolio_items = portfolio_item.objects.all()
    template_name = 'portfolio.html'
    context = {
        'portfolio_items':portfolio_items
    }
    return render(request, template_name, context)