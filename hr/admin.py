from django.contrib import admin

from hr.models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    class Meta:
        model = Applicant


admin.site.register(Applicant, ApplicantAdmin)
