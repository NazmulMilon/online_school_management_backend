from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Course, Enrolment, Attendance
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from users.serializers import StudentListAllSerializer


class StudentSerializer(ModelSerializer):
    fullname = SerializerMethodField()

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    class Meta:
        model = UserProfile
        fields = ["roll", 'fullname']


class CourseListSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']


class CourseRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class EnrolmentSerializer(ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class EnrolmentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()
    course = SerializerMethodField()

    def get_course(self, instance):
        course_id_list = []
        enrol_qs = Enrolment.objects.filter(user=instance.user).values("course")
        for item in enrol_qs:
            if item["course"] not in course_id_list:
                course_id_list.append(item["course"])
        course_queryset = Course.objects.filter(pk__in=course_id_list)
        return CourseListSerializer(course_queryset, many=True).data

    def get_user(self, instance):
        return instance.user.id

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else ""

    class Meta:
        model = Enrolment
        exclude = ['id', 'created_at', 'updated_at']


class EnrolmentRetrieveByCourseSerializer(ModelSerializer):
    user = SerializerMethodField()
    course_code = SerializerMethodField()
    course_name = SerializerMethodField()
    total_enrollment = SerializerMethodField()

    def get_user(self, instance):
        user_id_list = []
        enrolment_qs = Enrolment.objects.filter(course=instance.course).values('user_id')
        for item in enrolment_qs:
            if item["user_id"] not in user_id_list:
                user_id_list.append(item["user_id"])
        user_queryset = UserProfile.objects.filter(pk__in=user_id_list)
        return UserProfileListSerializer(user_queryset, many=True).data

    def get_course_code(self, instance):
        return instance.course.course_code if instance.course else ""

    def get_course_name(self, instance):
        return instance.course.course_name if instance.course else ""

    def get_total_enrollment(self, instance):
        enrolment_qs = Enrolment.objects.filter(course=instance.course).values('user_id')
        return len(enrolment_qs)

    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class UserRetrieveSerializer(ModelSerializer):
    course = SerializerMethodField()

    def get_course(self, instance):
        queryset = Course.objects.filter(id=instance.course_id)
        return CourseListSerializer(queryset, many=True).data

    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class UserProfileListSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at', 'father_name', "date_of_birth", 'mother_name', 'phone_no', 'user_role',
                   'address', 'parent']


class AttendanceCreateSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ['created_at', 'updated_at']


class AttendanceListSerializer(ModelSerializer):
    teacher = SerializerMethodField()
    course_code = SerializerMethodField()
    course_name = SerializerMethodField()
    student = SerializerMethodField()

    def get_teacher(self, instance):
        return instance.teacher.username if instance.teacher else ""

    def get_course_code(self, instance):
        return instance.course.course_code if instance.course else ""

    def get_course_name(self, instance):
        return instance.course.course_name if instance.course else ""

    def get_student(self, instance):
        return instance.student.username if instance.student else ""

    class Meta:
        model = Attendance
        exclude = ['course', 'created_by', 'updated_by']
