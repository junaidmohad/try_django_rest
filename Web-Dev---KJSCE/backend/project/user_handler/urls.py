from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('faculty', views.facultyViewSet, basename='faculty')
router.register('staff', views.staffViewSet, basename='staff')
router.register('student', views.studentViewSet, basename='student')

from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    # path('', views.facultyViewSet.as_view()),
]