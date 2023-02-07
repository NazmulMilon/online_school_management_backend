from django.urls import path
from .views import CourseListAPIView, EnrollmentListAPIView, EnrollmentCreateAPIView, EnrolmentRetrieveAPIView

urlpatterns = [
    path('course/all/', CourseListAPIView.as_view(), name='all_course'),


    # enrollment
    path('enrollment/all/', EnrollmentListAPIView().as_view(), name='all_enrollment'),
    path('enrollment/create/', EnrollmentCreateAPIView.as_view(), name='create_enrollment'),
    path('enrolment/retrieve/<int:user>/', EnrolmentRetrieveAPIView.as_view(), name='retrieve_enrollment'),
]