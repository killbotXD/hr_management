from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    doc = models.FileField(upload_to='', null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
