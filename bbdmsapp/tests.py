from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from tempfile import TemporaryDirectory

from .models import Bloodgroup, CustomUser, DonorReg


class BloodGroupSelectionTests(TestCase):
    def test_donor_signup_shows_seeded_blood_groups(self):
        response = self.client.get(reverse("donorsignup"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            Bloodgroup.objects.order_by("bloodgroup"),
            ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"],
            transform=lambda group: group.bloodgroup,
        )
        for group in Bloodgroup.objects.all():
            self.assertContains(
                response,
                f'<option value="{group.id}">{group.bloodgroup}</option>',
                html=True,
            )

    def test_donor_signup_saves_selected_blood_group(self):
        group = Bloodgroup.objects.get(bloodgroup="O+")
        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.post(
                    reverse("donorsignup"),
                    {
                        "pic": SimpleUploadedFile(
                            "donor.png", b"profile-image", content_type="image/png"
                        ),
                        "first_name": "Test",
                        "last_name": "Donor",
                        "username": "test-donor",
                        "email": "test-donor@example.com",
                        "mobno": "1234567890",
                        "age": "25",
                        "bg_id": str(group.id),
                        "gender": "Other",
                        "address": "Test address",
                        "password": "test-password-123",
                    },
                )

        self.assertRedirects(response, reverse("donorsignup"))
        donor = DonorReg.objects.get(admin__username="test-donor")
        self.assertEqual(donor.bloodgroup, group)


class EmptyProfilePictureTests(TestCase):
    def test_dashboard_renders_for_admin_without_profile_picture(self):
        admin = CustomUser.objects.create_superuser(
            username="jatin",
            email="jatin@localhost",
            password="jatin123",
        )
        self.client.force_login(admin)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "assets/img/profile.jpg")

# Create your tests here.
