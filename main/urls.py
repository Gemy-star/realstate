from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('faq', views.faq_page, name='faq-page'),
    path('about', views.about_page, name='about-page'),
    path('contact', views.contact_page, name='contact-page'),

]