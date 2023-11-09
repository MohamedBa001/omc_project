from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id","course_name","course_code","speciality_name")

    def speciality_name(self,object):
        return object.speciality.speciality_code
    
admin.site.register(Course,CourseAdmin)   

