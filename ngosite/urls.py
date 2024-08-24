# ngosite/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer_login/', views.volunteer_login, name='volunteer_login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('volunteers/', include('volunteers.urls')),  # Include the volunteers app URLs
]
