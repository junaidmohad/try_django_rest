from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.forms import 

from . import models
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class facultyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.Faculty_serializer

    def put(self, request, id=None):
        faculty = models.Faculty.objects.all()
        serializer = serializers.Faculty_serializer(faculty, data=request.data)
        return Response(serializer.data)


class staffViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Staff.objects.all()
    serializer_class = serializers.Staff_serializer

    def put(self, request, id=None):
        staff = models.Staff.objects.all()
        serializer = serializers.Staff_serializer(staff, data=request.data)
        return Response(serializer.data)


class studentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Student.objects.all()
    serializer_class = serializers.Student_serializer

    def put(self, request, id=None):
        student = models.Student.objects.all()
        serializer = serializers.Student_serializer(student, data=request.data)
        return Response(serializer.data)


#view funciton for logging out a user
def logout_view(request):
    logout(request)
    return redirect('home')