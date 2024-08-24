# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, 'volunteers/dashboard.html')

def edit_profile(request):
    return render(request, 'volunteers/profile_edit.html')

def submit_complaint(request):
    return render(request, 'volunteers/complaint_submission.html')

def package_status(request):
    return render(request, 'volunteers/package_status.html')

def message_inbox(request):
    return render(request, 'volunteers/message_inbox.html')
