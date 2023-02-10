from django.contrib import admin

from .models import Course, Enrolment, Attendance

admin.site.register(Course)
admin.site.register(Enrolment)
admin.site.register(Attendance)
