# ngosite/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from volunteers.models import VolunteerUser

def index(request):
    return render(request, 'index.html', {'active_page': 'home'})

def faq(request):
    return render(request, 'faq.html', {'active_page': 'faq'})

def contact(request):
    return render(request, 'contact.html', {'active_page': 'contact'})

def volunteer(request):
    return render(request, 'volunteer.html', {'active_page': 'volunteer'})

def about(request):
    return render(request, 'about.html', {'active_page': 'about'})

def volunteer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and isinstance(user, VolunteerUser):
            login(request, user)
            return redirect('volunteer_dashboard')  # Use 'volunteer_dashboard'
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('volunteer_login')
    
    return render(request, 'login.html')

class LogoutView(DjangoLogoutView):
    next_page = 'home'