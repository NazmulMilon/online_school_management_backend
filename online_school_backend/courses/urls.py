from django.urls import path
from .views import CourseListAPIView, EnrollmentListAPIView

urlpatterns = [
    path('course/all/', CourseListAPIView.as_view(), name='all_course'),


    # enrollment
    path('enrollment/all/', EnrollmentListAPIView().as_view(), name='all_enrollment'),
]