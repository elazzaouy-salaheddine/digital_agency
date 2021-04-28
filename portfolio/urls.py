from django.urls import path
from .views import portfolio_page,portfolio_detail

urlpatterns = [
    path('',portfolio_page, name='portfolio'),
    path('<int:id>/', portfolio_detail, name='portfolio_detail'),
]