from django.db import models

from django.contrib.auth.models import User
from systems.models import BaseModel


class Course(BaseModel):
    course_code = models.CharField(max_length=10, help_text='Course code')
    course_name = models.CharField(max_length=100, help_text='course name')

    class Meta:
        db_table = 'courses'
