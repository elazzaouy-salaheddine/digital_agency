from django.urls import path
from .views import about_page,privacy_policy,terms_of_service

urlpatterns = [
    path('',about_page, name='about'),
    path('terms-of-service/',terms_of_service, name='terms_of_service'),
    path('privacy-policy/',privacy_policy, name='privacy_policy'),
]