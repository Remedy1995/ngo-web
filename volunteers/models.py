from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    volunteers = models.ManyToManyField('VolunteerUser', related_name='organizations')

    def __str__(self):
        return self.name


class VolunteerUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, default='N/A', blank=False)
    country = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)  # Allow empty values
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)  # Allow empty values

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Package(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('received', 'Received'),
    ]
    
    volunteer = models.ForeignKey(VolunteerUser, on_delete=models.CASCADE, related_name='packages')
    tracking_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipped_date = models.DateField(null=True, blank=True)
    received_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Package {self.tracking_number} - {self.status}"

class Complaint(models.Model):
    volunteer = models.ForeignKey(VolunteerUser, on_delete=models.CASCADE, related_name='complaints')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    submitted_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('resolved', 'Resolved'),
    ], default='submitted')

    def __str__(self):
        return f"Complaint from {self.volunteer} - {self.subject}"

    class Meta:
        ordering = ['-submitted_date']

class Message(models.Model):
    volunteer = models.ForeignKey(VolunteerUser, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.volunteer} - {self.subject}"

    class Meta:
        ordering = ['-sent_date']