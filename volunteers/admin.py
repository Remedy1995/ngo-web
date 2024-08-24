from django.contrib import admin
from .models import VolunteerUser, Message, Complaint, Organization, Package

admin.site.register(VolunteerUser)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'subject', 'sent_date', 'is_read')
    list_filter = ('is_read', 'sent_date')
    search_fields = ('subject', 'body')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'subject', 'submitted_date', 'status')
    list_filter = ('status', 'submitted_date')
    search_fields = ('subject', 'description')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'tracking_number', 'status', 'shipped_date', 'received_date')
    list_filter = ('status', 'shipped_date', 'received_date')
    search_fields = ('tracking_number', 'notes')