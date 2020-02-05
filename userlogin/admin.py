from django.contrib import admin
from .models import Applicant, Absent

admin.site.register(Applicant)
admin.site.register(Absent)