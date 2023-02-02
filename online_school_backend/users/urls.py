from django.urls import path
from .views import UserProfileRetrieveAPIView, UserProfileCreateAPIView, UserProfileListAPIView, StudentListAllAPIView

urlpatterns = [
    path('userprofile/all/', UserProfileListAPIView.as_view(), name="all_userprofile"),
    path('userprofile/create/', UserProfileCreateAPIView.as_view(), name="create_userprofile"),
    path('userprofile/retrieve/<int:value>/', UserProfileRetrieveAPIView.as_view(), name="retrieve_userprofile"),

    # search student
    path('userprofile/all/<str:STUDENT>/', StudentListAllAPIView.as_view(), name="all students"),

]
