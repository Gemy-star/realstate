from django.shortcuts import render, redirect
from realstate import models
from .models import FAQ, Contact


def home_page(request):

    return render(request, 'main/home.html')


def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'main/faqs.html', context={"questions": faqs})


def about_page(request):
    return render(request, 'main/about.html')


def staff_page(request):
    return render(request, 'main/staff.html')

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        if contact.pk:
            return redirect('home-page')
    return render(request, 'main/contact.html')
