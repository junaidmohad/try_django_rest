from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

from .models import *
# from .models import CustomUser

# class CustomeUserAdmin(UserAdmin):
#     list_display = ('email', 'date_joined', 'last_login', 'date_joined', 'last_login')
#     search_fields = ('email', 'date_joined')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

#     ordering = ('email',)
    
admin.site.register(Role)
admin.site.register(CustomUser)
admin.site.register(Branch)
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Year)