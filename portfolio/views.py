from django.http import Http404
from django.shortcuts import render
from .models import portfolio_item, category


def portfolio_page(request):
    portfolio_items = portfolio_item.objects.all()
    categorys = category.objects.all()
    template_name = 'portfolio.html'
    context = {
        'portfolio_items':portfolio_items,
        'categorys':categorys
    }
    return render(request, template_name, context)


def portfolio_detail(request,id):
    try:
        portfolio_items = portfolio_item.objects.get(id=id)
    except portfolio_item.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'portfolio_detail.html', {'portfolio_item': portfolio_items})