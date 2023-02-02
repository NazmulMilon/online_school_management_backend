from django.db import models
from django.contrib.auth.models import User
from systems.models import BaseModel
from systems.enums import UserType


# Create your models here.

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="user")
    father_name = models.CharField(max_length=100, help_text="user's father name")
    mother_name = models.CharField(max_length=100, help_text="user's mother name ")
    date_of_birth = models.DateField(auto_now_add=True, help_text="user's date of birth")
    phone_no = models.IntegerField(help_text="user's phone number")
    user_type = models.CharField(max_length=10, choices=UserType.choices(), default=UserType.STUDENT_TYPE.value)
    address = models.CharField(max_length=100, help_text="user's address")
    roll = models.IntegerField(help_text="student's roll number")

    class Meta:
        db_table = 'user_profiles'
