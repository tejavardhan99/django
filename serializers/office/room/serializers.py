from rest_framework import serializers
from .models import Student, Teacher, School,Different_Model,Enough,User,Session_Model


class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class get_teacher_serializer(serializers.ModelSerializer):
    student_details = student_serializer(source="student_id")  # Ensure `student_id` exists in Teacher model
    teacher_details = teacher_serializer()  # No need for `source="*"`

    class Meta:
        model = Teacher
        fields = ["student_details", "teacher_details"]


class school_serializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class get_master_serializer(serializers.ModelSerializer):
    master = get_teacher_serializer(source="teacher_id")  # Fixed "techer_id" typo

    class Meta:
        model = School
        fields = ["master"]



class Image_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Different_Model
        fields='__all__'


class Enough_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Enough
        fields="__all__"
    



# class User_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
        



class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Jwt_Login_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]


class Session_serializer(serializers.ModelSerializer):
    class Meta:
        model=Session_Model
        fields='__all__'
    