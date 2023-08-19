from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user_handler.forms import AccountAuthenticationForm, AccountUpdateForm
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

#this view function inflates the login form that we just created
def login_view(request):
    context = {}
    user =  request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
        else:
            form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user_handler/login.html', context)              #we need to change this render function as per the frontend naming for login page


#this view function is reponsible for updating the details of the respective user
def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)               #the instance used here is to look for the primary key of the user that is authenticated. this instance refernces back to the instance in the forms.py
        if form.is_valid():
            form.save()

    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username
            }
        )

    context['account_form'] = form
    return render(request, 'account/account.html', context)             #we need to change this too to update page as per the project repo