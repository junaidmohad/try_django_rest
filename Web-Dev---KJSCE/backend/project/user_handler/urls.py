from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('faculty', views.facultyViewSet, basename='faculty')
router.register('staff', views.staffViewSet, basename='staff')
router.register('student', views.studentViewSet, basename='student')

from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name="home"),
    
    path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),


    # path('', views.facultyViewSet.as_view()),
]