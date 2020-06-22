from django.forms import ModelForm

from hr.models import Applicant


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ('approved',)
