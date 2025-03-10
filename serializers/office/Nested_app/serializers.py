from rest_framework import serializers
from .models import User, UserRegistration, LocationDetails, UserProfileDetails, PersonalDetails, CodeSet

class CodeSetSerializer(serializers.Serializer):
    CodeType = serializers.CharField(max_length=50)
    CodeValue = serializers.CharField(max_length=50)

class PersonalDetailsSerializer(serializers.Serializer):
    ProfilePic = serializers.URLField()
    UserName = serializers.CharField(max_length=100)
    DoB = serializers.DateField()
    Gender = serializers.CharField(max_length=10)
    CodeSet = CodeSetSerializer()

class UserRegistrationSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Email = serializers.EmailField()
    Phone = serializers.CharField(max_length=20)
    Password = serializers.CharField(max_length=100)
    PersonalDetails = PersonalDetailsSerializer()

class LocationDetailsSerializer(serializers.Serializer):
    Country = serializers.CharField(max_length=100)
    State = serializers.CharField(max_length=100)
    District = serializers.CharField(max_length=100)
    Pincode = serializers.CharField(max_length=10)
    Address = serializers.CharField()

class UserProfileDetailsSerializer(serializers.Serializer):
    ShortBrief = serializers.CharField()
    LongBrief = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    UserRegistration = UserRegistrationSerializer()
    LocationDetails = LocationDetailsSerializer()
    UserProfileDetails = UserProfileDetailsSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_registration_data = validated_data.pop('UserRegistration')
        location_data = validated_data.pop('LocationDetails')
        profile_data = validated_data.pop('UserProfileDetails')

        user = User.objects.create(**validated_data)

        user.UserRegistration = UserRegistration(**user_registration_data)
        user.LocationDetails = LocationDetails(**location_data)
        user.UserProfileDetails = UserProfileDetails(**profile_data)

        user.save()
        return user
