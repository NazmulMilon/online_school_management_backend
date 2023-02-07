from django.contrib import admin

from .models import Course, Enrolment

admin.site.register(Course)
admin.site.register(Enrolment)
