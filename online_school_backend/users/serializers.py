from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField


class UserProfileCreateSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()
    password = SerializerMethodField()
    fullname = SerializerMethodField()

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_last_name(self, instance):
        return instance.user.last_name

    def get_email(self, instance):
        return instance.user.email

    def get_password(self, instance):
        return instance.user.password

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at']


class UserProfileListSerializer(ModelSerializer):
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
        exclude = ['created_at', 'updated_at', 'father_name', 'mother_name', 'roll']


class UserProfileRetrieveSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()

    def get_first_name(self, instance):
        return instance.user.first_name if instance.user else None

    def get_last_name(self, instance):
        return instance.user.last_name if instance.user else None

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    class Meta:
        model = UserProfile
        fields = ["roll", "first_name", "last_name", "fullname", "email", "username", "father_name", "mother_name",
                  "date_of_birth", "phone_no", "user_role", "address"]


class TeacherListAllSerializer(ModelSerializer):
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "email", "username", "phone_no", "user_role"]


class ParentListSerializer(ModelSerializer):
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "email", "username", "phone_no", "user_role"]


class StudentSerializer(ModelSerializer):
    # parent = SerializerMethodField()
    #
    # def get_parent(self, instance):
    #     parent_obj = UserProfile.objects.filter(id=instance.parent_id).first()
    #     return StudentRetrieveSerializer(parent_obj).data

    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at', 'parent']


class ParentRetrieveSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()

    parent = SerializerMethodField()

    def get_first_name(self, instance):
        return instance.user.first_name if instance.user else None

    def get_last_name(self, instance):
        return instance.user.last_name if instance.user else None

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    def get_parent(self, instance):
        parent_obj = UserProfile.objects.filter(id=instance.parent_id).first()
        return StudentSerializer(parent_obj).data

    class Meta:
        model = UserProfile
        # fields = ["roll", "first_name", "last_name", "fullname", "email", "username", "father_name", "mother_name",
        #           "date_of_birth", "phone_no", "user_role", "address"]
        exclude = ['created_at', 'updated_at', 'roll']


class StudentListAllSerializer(ModelSerializer):
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    class Meta:
        model = UserProfile
        fields = ["id", "roll", "fullname", "email", "username", "phone_no", "user_role"]


class ParentSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['created_at', 'updated_at', 'parent', 'roll']


class StudentRetrieveSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()
    fullname = SerializerMethodField()
    username = SerializerMethodField()
    parent = SerializerMethodField()

    def get_first_name(self, instance):
        return instance.user.first_name if instance.user else None

    def get_last_name(self, instance):
        return instance.user.last_name if instance.user else None

    def get_email(self, instance):
        return instance.user.email if instance.user else None

    def get_fullname(self, instance):
        name = ""
        if instance.user.first_name:
            name += instance.user.first_name + " "
        if instance.user.last_name:
            name += instance.user.last_name
        return name

    def get_username(self, instance):
        return instance.user.username if instance.user else None

    def get_parent(self, instance):
        parent_obj = UserProfile.objects.filter(parent=instance).first()
        return ParentSerializer(parent_obj).data

    class Meta:
        model = UserProfile
        # fields = ["roll", "first_name", "last_name", "fullname", "email", "username", "father_name", "mother_name",
        #           "date_of_birth", "phone_no", "user_role", "address", "parent"]

        exclude = ['created_at', 'updated_at']
