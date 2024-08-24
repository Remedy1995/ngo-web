from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['tracking_number', 'status', 'shipped_date', 'received_date', 'notes']
