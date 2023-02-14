from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Course, Enrolment, Attendance
from .serializers import CourseCreateSerializer, CourseRetrieveSerializer, CourseListSerializer, \
    EnrolmentListSerializer, UserRetrieveSerializer, EnrolmentSerializer, EnrollmentSerializer, \
    EnrolmentRetrieveByCourseSerializer, AttendanceListSerializer, AttendanceCreateSerializer, \
    AttendanceRetrieveSerializer
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


class EnrolmentRetrieveAPIView(ListAPIView):
    serializer_class = EnrolmentListSerializer
    queryset = Enrolment.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('user', None)
        data = dict()
        queryset = Enrolment.objects.filter(user_id=pk).first()

        # course_list = []
        # for item in queryset:
        #     course_data = dict()
        #     course_data["id"] = item.course.id
        #     course_data["course_code"] = item.course.course_code
        #     course_data["course_name"] = item.course.course_name
        #     course_list.append(course_data)
        #
        # data["user"] = pk
        # data["course"] = course_list
        serializer = EnrolmentListSerializer(queryset, many=False)
        # return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EnrolmentRetrieveByCourseAPIView(RetrieveAPIView):
    serializer_class = EnrolmentRetrieveByCourseSerializer
    queryset = Enrolment.objects.all()

    def get(self, request, *args, **kwargs):
        course = kwargs.get('course', None)
        enrolment_obj = Enrolment.objects.filter(course_id=course).first()
        # data = dict()
        # user_list = []
        # queryset = Enrolment.objects.filter(course_id=course)
        # amount = len(queryset)
        # for item in queryset:
        #     user_dict={}
        #     user_dict["user_id"] = item.user_id
        #     user_dict["user_name"] = item.user.first_name
        #     user_list.append(user_dict)
        # data["course"] = course
        # data["total_enrollment"] = amount
        # data["user"] = user_list
        #
        # # serializer = EnrolmentRetrieveByCourseSerializer(queryset)
        serializer = EnrolmentRetrieveByCourseSerializer(enrolment_obj)
        # return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EnrollmentCreateAPIView(CreateAPIView):
    queryset = Enrolment.objects.all()
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = data.get('user', None)
        user_obj = UserProfile.objects.filter(id=user, user_role='STUDENT').first()
        if not user_obj:
            return Response(data={'details': 'User does not found.'}, status=status.HTTP_404_NOT_FOUND)

        course = data.get('course', None)
        course_obj = Course.objects.filter(id=course).exists()
        if not course_obj:
            return Response(data={'details': 'Course ID does not matched. Enter valid course id'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        exist_obj = Enrolment.objects.filter(user=user, course=course).exists()
        if exist_obj:
            return Response(data={'details': 'User already have taken the course.'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        enrollment_obj = Enrolment(user_id=user, course_id=course)
        enrollment_obj.save()
        serializer = EnrollmentSerializer(enrollment_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EnrollmentListAPIView(ListAPIView):
    queryset = Enrolment.objects.all()
    serializer_class = EnrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Enrolment.objects.all()
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AttendanceCreateAPIView(CreateAPIView):
    serializer_class = AttendanceCreateSerializer
    queryset = Attendance.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        teacher = data.get('teacher', None)
        if teacher is None:
            return Response(data={'details': 'Teacher name required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if not UserProfile.objects.filter(user_id=teacher, user_role="TEACHER").exists():
            return Response(data={'details': 'Teacher not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        course = data.get('course', None)
        if course is None:
            return Response(data={'details': 'Course required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if not Course.objects.filter(id=course).exists():
            return Response(data={'details': 'course not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        student = data.get('student', None)
        if student is None:
            return Response(data={'details': 'Student name required.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if not UserProfile.objects.filter(id=student, user_role="STUDENT").exists():
            return Response(data={'details': 'student does not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        is_present = data.get('is_present', None)

        attendance_obj = Attendance(teacher_id=teacher, course_id=course, student_id=student, is_present=is_present,
                                    created_by_id=teacher, updated_by_id=teacher)
        attendance_obj.save()
        serializer = AttendanceCreateSerializer(attendance_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class AttendanceRetrieveAPIView(RetrieveAPIView):
    serializer_class = AttendanceRetrieveSerializer
    queryset = Attendance.objects.all()

    def get(self, request, *args, **kwargs):
        course = kwargs.get('pk', None)
        attendance_obj = Attendance.objects.filter(course_id=course).first()
        serializer = AttendanceRetrieveSerializer(attendance_obj, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AttendanceListAPIView(ListAPIView):
    serializer_class = AttendanceListSerializer
    queryset = Attendance.objects.all()

    def get(self, request, *args, **kwargs):
        date = request.data.get('date', None)
        queryset = Attendance.objects.filter(created_at__date=date).all()
        # queryset = Attendance.objects.all()
        serializer = AttendanceListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)