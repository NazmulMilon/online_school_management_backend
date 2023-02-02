from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from systems.enums import UserType
from .serializers import UserProfileListSerializer, UserProfileRetrieveSerializer, UserProfileCreateSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset
        serializer = UserProfileListSerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


