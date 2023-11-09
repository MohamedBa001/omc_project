from django.contrib import admin
from .models import Student,Professor
 # main_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","email","date_of_birth","speciality")
    
    def  full_name(self,object):
        return object.get_full_name()
    
    def email(self,object):
        return object.user.email 


    def speciality(self,object):
        return object.speciality.speciality_code
    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","email","date_of_birth")  

    def  full_name(self,object):
        return object.get_full_name()  
    
    def email(self,object):
        return object.user.email 


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'user_type', 'gender', 'is_active', 'is_staff', 'created', 'updated')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    list_filter = ('is_active', 'is_staff', 'user_type', 'gender')
   

admin.site.register(CustomUser, CustomUserAdmin)
     

admin.site.register(Student,StudentAdmin)
admin.site.register(Professor,ProfessorAdmin) 


