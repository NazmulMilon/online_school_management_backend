from django.db import models

from django.contrib.auth.models import User
from users.models import UserProfile
from systems.models import BaseModel
from systems.enums import AttendanceType


class Course(BaseModel):
    course_code = models.CharField(max_length=10, help_text='Course code')
    course_name = models.CharField(max_length=100, help_text='course name')

    class Meta:
        db_table = 'courses'


class Enrolment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollment_user")
    course = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_enrollment")

    class Meta:
        db_table = 'enrolments'


class Attendance(BaseModel):
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_teachers")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_details")
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="user_student")
    is_present = models.BooleanField(default=False, help_text="student absent or present")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="user_created_attendance")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="user_updated_attendance")

    class Meta:
        db_table = 'attendances'
