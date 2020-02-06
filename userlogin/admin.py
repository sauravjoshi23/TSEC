from django.contrib import admin
from .models import Applicant, Absent, School

admin.site.register(Applicant)
admin.site.register(Absent)
admin.site.register(School)