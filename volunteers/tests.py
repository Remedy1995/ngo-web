from django.test import TestCase
from .models import VolunteerUser, Organization
from django.utils.crypto import get_random_string

class VolunteerUserModelTest(TestCase):
    def setUp(self):
        # Create an Organization instance for use in tests
        self.organization = Organization.objects.create(name="Test Org")
        
        # Generate unique usernames
        unique_suffix = get_random_string(length=6)
        self.volunteer_with_picture = VolunteerUser.objects.create(
            username=f'uniqueuser1_{unique_suffix}',
            password='password123',
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            address="123 Test St",
            country="Test Country",
            passport_number="A1234567",
            picture="path/to/picture.jpg",  # Picture field with a value
            organization=self.organization
        )
        
        self.volunteer_without_picture = VolunteerUser.objects.create(
            username=f'uniqueuser2_{unique_suffix}',
            password='password123',
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            phone_number="0987654321",
            address="456 Test Ave",
            country="Test Country",
            passport_number="B7654321",
            organization=self.organization
        )

    def test_volunteer_creation(self):
        # Test that all fields are correctly saved
        self.assertEqual(self.volunteer_with_picture.first_name, "John")
        self.assertEqual(self.volunteer_with_picture.last_name, "Doe")
        self.assertEqual(self.volunteer_with_picture.email, "john.doe@example.com")
        self.assertEqual(self.volunteer_with_picture.phone_number, "1234567890")
        self.assertEqual(self.volunteer_with_picture.address, "123 Test St")
        self.assertEqual(self.volunteer_with_picture.country, "Test Country")
        self.assertEqual(self.volunteer_with_picture.passport_number, "A1234567")
        self.assertEqual(self.volunteer_with_picture.organization.name, "Test Org")

    def test_string_representation(self):
        # Test the string representation of the VolunteerUser instance
        self.assertEqual(str(self.volunteer_with_picture), "John Doe")

    def test_volunteer_with_picture(self):
        # Test that the picture field is correctly saved when provided
        self.assertEqual(self.volunteer_with_picture.picture.name, "path/to/picture.jpg")
        self.assertEqual(self.volunteer_with_picture.organization, self.organization)

    def test_volunteer_without_picture(self):
        # Debug output
        print(f"Picture Field Value: {self.volunteer_without_picture.picture.name}")
        
        # Test that the picture field is properly handled when not provided
        picture_name = self.volunteer_without_picture.picture.name
        self.assertTrue(picture_name == '' or picture_name is None)
        self.assertEqual(self.volunteer_without_picture.organization, self.organization)
