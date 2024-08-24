from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'active_page': 'home'})

def faq(request):
    return render(request, 'faq.html', {'active_page': 'faq'})

def contact(request):
    return render(request, 'contact.html', {'active_page': 'contact'})

def about(request):
    return render(request, 'about.html', {'active_page': 'about'})

def volunteer(request):
    return render(request, 'volunteer.html', {'active_page': 'volunteer'})

def volunteer_login(request):
    return render(request, 'volunteer_login.html', {'active_page': 'volunteer_login'})
