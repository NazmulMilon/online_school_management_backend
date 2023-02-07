from django.db import models

from django.contrib.auth.models import User
from systems.models import BaseModel


class Course(BaseModel):
    course_code = models.CharField(max_length=10, help_text='Course code')
    course_name = models.CharField(max_length=100, help_text='course name')

    class Meta:
        db_table = 'courses'


class Enrolment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=' user name')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, help_text='available courses')

    class Meta:
        db_table = 'enrolments'
