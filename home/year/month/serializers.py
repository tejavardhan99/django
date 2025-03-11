from rest_framework import serializers

from .models import Student

class Master(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["firstname","password"]
    


