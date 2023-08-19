from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

from .models import *
# from .models import CustomUser

#this class helps for searching data based on certian field values 
class CustomeUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Role)
admin.site.register(CustomUser, CustomeUserAdmin)
admin.site.register(Branch)
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Year)