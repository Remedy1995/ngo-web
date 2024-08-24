from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView
from .models import Package
from .forms import PackageForm

@login_required
def dashboard(request):
    user = request.user
    # Assuming you have methods to get packages, complaints, messages, and recent activities
    packages = user.packages.all()
    complaints = user.complaints.all()
    messages = user.messages.all()
    recent_activities = get_recent_activities(user)  # Replace with your method to fetch recent activities

    context = {
        'volunteer': user,
        'packages': packages,
        'complaints': complaints,
        'messages': messages,
        'recent_activities': recent_activities
    }

    return render(request, 'volunteers/dashboard.html', context)

def edit_profile(request):
    return render(request, 'volunteers/profile_edit.html')

def submit_complaint(request):
    return render(request, 'volunteers/complaint_submission.html')

def package_status(request):
    return render(request, 'volunteers/package_status.html')

def message_inbox(request):
    return render(request, 'volunteers/message_inbox.html')

# Define or import the get_recent_activities function as needed
def get_recent_activities(user):
    # Placeholder for your logic to get recent activities
    return []



class PackageListView(ListView):
    model = Package
    template_name = 'volunteers/package_list.html'
    context_object_name = 'packages'

class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'volunteers/package_form.html'
    success_url = '/packages/'  # Redirect after successful update

    def get_object(self):
        return get_object_or_404(Package, pk=self.kwargs['pk'])

