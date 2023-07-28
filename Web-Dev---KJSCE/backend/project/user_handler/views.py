from django.shortcuts import render
from . import models
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers

# Create your views here.


class facultyViewSet(viewsets.ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.Faculty_serializer

    def put(self, request, id=None):
        faculty = models.Faculty.objects.all()
        serializer = serializers.Faculty_serializer(faculty, data=request.data)
        return Response(serializer.data)


class staffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.Staff_serializer

    def put(self, request, id=None):
        staff = models.Staff.objects.all()
        serializer = serializers.Staff_serializer(staff, data=request.data)
        return Response(serializer.data)


class studentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.Student_serializer

    def put(self, request, id=None):
        student = models.Student.objects.all()
        serializer = serializers.Student_serializer(student, data=request.data)
        return Response(serializer.data)
