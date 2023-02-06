from django.urls import path
from .views import UserProfileRetrieveAPIView, UserProfileCreateAPIView, UserProfileListAPIView, StudentListAllAPIView, \
    StudentRetrieveAPIView, TeacherListAllAPIView, ParentListAllAPIView, ParentRetrieveAPIView

urlpatterns = [
    path('userprofile/all/', UserProfileListAPIView.as_view(), name="all_userprofile"),
    path('userprofile/create/', UserProfileCreateAPIView.as_view(), name="create_userprofile"),
    path('userprofile/retrieve/<int:value>/', UserProfileRetrieveAPIView.as_view(), name="retrieve_userprofile"),

    # student
    path('student/all/<str:STUDENT>/', StudentListAllAPIView.as_view(), name="all_students"),
    path('student/retrieve/<int:pk>/', StudentRetrieveAPIView.as_view(), name="retrieve_student"),

    # teachers
    path('teacher/all/<str:TEACHER>/', TeacherListAllAPIView.as_view(), name="all_teachers"),

    # parents
    path('parent/all/', ParentListAllAPIView.as_view(), name="all_parents"),
    path('parent/detail/<int:pk>/', ParentRetrieveAPIView.as_view(), name="retrieve_parent"),




]
