from django.test import TestCase, Client
from django.urls import reverse

from hr.models import Applicant


class TestViews(TestCase):
    def test_1(self):
        client = Client()
        self.applicant = Applicant.objects.create(id=9999)

        response = client.get(reverse('approve', args=['9999']))
        self.assertEquals(response.status_code, 200)
        self.applicant.refresh_from_db()
        self.assertEquals(self.applicant.approved, True)

    def test_2(self):
        client = Client()
        self.applicant1 = Applicant.objects.create(name="Soham", email="sonawane.1@iitj.ac.in")

        response = client.get(reverse('login'))

        self.assertContains(response, "Soham")
        self.assertContains(response, "sonawane.1@iitj.ac.in")
