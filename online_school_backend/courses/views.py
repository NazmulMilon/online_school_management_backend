from django.shortcuts import render
from .models import Course
from .serializers import CourseCreateSerializer, CourseRetrieveSerializer, CourseListSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status


class CourseListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        serializer = CourseListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
