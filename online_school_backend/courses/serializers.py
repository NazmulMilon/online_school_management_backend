from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Course, Enrolment, Attendance
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from users.serializers import StudentListAllSerializer
from rest_framework import serializers


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


class EnrollmentRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class UserProfileListSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at', 'father_name', "date_of_birth", 'mother_name', 'phone_no', 'user_role',
                   'address', 'parent']


class AttendanceSerializer(ModelSerializer):
    # roll = SerializerMethodField()
    # fullname = SerializerMethodField()
    #
    # def get_roll(self, instance):
    #     student_obj = UserProfile.objects.filter(user_id=instance.student).first()
    #     return student_obj.roll
    #
    # def get_fullname(self, instance):
    #     name = ""
    #     if instance.student.first_name:
    #         name += instance.student.first_name + " "
    #     if instance.student.last_name:
    #         name += instance.student.last_name
    #     return name
    #     # return instance.student.username if instance.student else ""

    class Meta:
        model = Attendance
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'course', 'teacher']


class AttendanceRetrieveSerializer(ModelSerializer):
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
        student_id_lst = []
        attendance_qs = Attendance.objects.filter(teacher_id=instance.teacher, course=instance.course, created_at__date=instance.created_at)
        for attendance_obj in attendance_qs:
            student_profile = UserProfile.objects.filter(user=attendance_obj.student).first()
            data_dict = {
                'student_id': attendance_obj.student_id,
                'student_name': attendance_obj.student.username,
                'is_present': attendance_obj.is_present,
                'roll': student_profile.roll if student_profile else ""
            }
            student_id_lst.append(data_dict)
        print(student_id_lst)
        return student_id_lst

    # def get_student(self, instance):
    #     queryset = Attendance.objects.filter(id=instance.student_id)
    #     return AttendanceSerializer(queryset, many=True).data

    # def get_student(self, instance):
    #     student_id_lst = []
    #     attendance_qs = Attendance.objects.filter(course=instance.course)
    #     for attendance_obj in attendance_qs:
    #         data_dict = {
    #             'student_id': attendance_obj.student_id,
    #             'student_name': attendance_obj.student.username,
    #             'is_present': attendance_obj.is_present,
    #             # 'roll': instance.student.userprofile.roll
    #         }
    #         student_id_lst.append(data_dict)
    #
    #     return TestSerializer(student_id_lst).data

    class Meta:
        model = Attendance
        exclude = ['course', 'is_present', 'created_by', 'updated_by']


class TestSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    student_name = serializers.CharField()
    is_present = serializers.BooleanField()
    # roll = serializers.IntegerField()


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
