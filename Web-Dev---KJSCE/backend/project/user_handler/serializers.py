from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


class Faculty_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = "__all__"


class Staff_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = "__all__"


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"
        depth = 1
