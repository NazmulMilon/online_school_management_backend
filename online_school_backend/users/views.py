from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from systems.enums import UserType
from .serializers import UserProfileListSerializer, UserProfileRetrieveSerializer, UserProfileCreateSerializer, \
    StudentListAllSerializer, StudentRetrieveSerializer, TeacherListAllSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction


# Create your views here.
class UserProfileCreateAPIView(CreateAPIView):
    serializer_class = UserProfileCreateSerializer
    queryset = UserProfile.objects.all()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        first_name = data.get('first_name', None)
        if first_name is None:
            return Response(data={'details': "User's first name required. "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        last_name = data.get('last_name', None)
        if last_name is None:
            return Response(data={'details': "User's last name required. "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        username = data.get('username', None)
        if User.objects.filter(username=username).exists():
            return Response(data={'details': 'Username already exists. '}, status=status.HTTP_406_NOT_ACCEPTABLE)
        father_name = data.get('father_name', None)
        if father_name is None:
            return Response(data={'details': "User's father's name required. "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        mother_name = data.get('mother_name', None)
        if mother_name is None:
            return Response(data={'details': "User's mother's name required. "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        email = data.get('mother_name', None)
        password = data.get('password', None)
        date_of_birth = data.get('date_of_birth', None)
        phone_no = data.get('phone_no', None)
        user_role = data.get('user_role', None)
        if user_role is None:
            return Response(data={'details': "User's role required. "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        address = data.get('address', None)
        # roll = data.get('roll', None)
        roll = None
        if user_role == "STUDENT":
            obj = UserProfile.objects.filter(user_role=user_role).last()
            if obj:
                roll = obj.roll + 1
            else:
                roll = 1
        else:
            roll = None
        user_obj = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user_obj.save()

        userprofile_obj = UserProfile(user=user_obj, father_name=father_name, mother_name=mother_name,
                                      date_of_birth=date_of_birth, phone_no=phone_no, user_role=user_role,
                                      address=address, roll=roll)
        userprofile_obj.save()
        serializer = UserProfileCreateSerializer(userprofile_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = UserProfile.objects.all()
        serializer = UserProfileListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserProfileRetrieveSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('value', None)
        user_obj = UserProfile.objects.filter(pk=pk).first()
        serializer = UserProfileRetrieveSerializer(user_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class StudentListAllAPIView(ListAPIView):
    serializer_class = StudentListAllSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        value = kwargs.get('STUDENT', None)
        if value != "STUDENT":
            return Response(data={'details': 'Student type wrong.'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = UserProfile.objects.filter(user_role=value).order_by('roll')
        serializer = StudentListAllSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class StudentRetrieveAPIView(RetrieveAPIView):
    serializer_class = StudentRetrieveSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        student_obj = UserProfile.objects.filter(pk=pk).first()
        serializer = StudentRetrieveSerializer(student_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TeacherListAllAPIView(ListAPIView):
    serializer_class = TeacherListAllSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        value = kwargs.get('TEACHER', None)

        teacher_queryset = UserProfile.objects.filter(user_role=value)
        serializer = TeacherListAllSerializer(teacher_queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ParentListAllAPIView(ListAPIView):
    serializer_class = ParentListSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        value = "PARENT"
        parent_queryset = UserProfile.objects.filter(user_role=value)
        serializer = ParentListSerializer(parent_queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)