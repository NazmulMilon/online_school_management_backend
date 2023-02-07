from django.urls import path
from .views import CourseListAPIView

urlpatterns = [
    path('course/all/', CourseListAPIView.as_view(), name='all_course'),
]