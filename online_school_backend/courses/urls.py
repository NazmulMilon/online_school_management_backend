from django.urls import path
from .views import CourseListAPIView, EnrollmentListAPIView, EnrollmentCreateAPIView, EnrolmentRetrieveAPIView, \
    EnrolmentRetrieveByCourseAPIView, AttendanceListAPIView, AttendanceRetrieveAPIView, AttendanceCreateAPIView

urlpatterns = [
    path('course/all/', CourseListAPIView.as_view(), name='all_course'),


    # enrollment
    path('enrollment/all/', EnrollmentListAPIView().as_view(), name='all_enrollment'),
    path('enrollment/create/', EnrollmentCreateAPIView.as_view(), name='create_enrollment'),
    path('enrolment/retrieve/<int:user>/', EnrolmentRetrieveAPIView.as_view(), name='retrieve_enrollment'),
    path('enrolment/retrieve/course/<int:course>/', EnrolmentRetrieveByCourseAPIView.as_view(),
         name='retrieve_enrolment_by_course'),

    # attendance
    path('attendance/course/<int:pk>/', AttendanceRetrieveAPIView.as_view(), name="retrieve_attendance"),
    path('attendance/all/', AttendanceListAPIView.as_view(), name="all_attendance"),
    path('attendance/create/', AttendanceCreateAPIView.as_view(), name="create_attendance"),
]