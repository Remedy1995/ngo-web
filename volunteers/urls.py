# volunteers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='volunteer_dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('package_status/', views.package_status, name='package_status'),
    path('message_inbox/', views.message_inbox, name='message_inbox'),
]
