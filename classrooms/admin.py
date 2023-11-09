from django.contrib import admin
from .models import Classroom
from .models import Session


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("id","classroom_type","classroom_number")

    def speciality_name(self,object):
        return object.speciality.speciality_code
    



class SessionsAdmin(admin.ModelAdmin):
    list_display = ("session_time","session_type","session_date","speciality","classroom","course","professor","groupe")

    def speciality(self,object):
        return object.speciality.speciality_code
    def classroom(self,object):
        return object.classroom.classroom_number
    def course(self,object):
        return object.course.course_code
    def professor(self,object):
        return object.professor.professor_name
    def groupe(self,object):
        return str(object.groupe)


admin.site.register(Classroom,ClassroomAdmin)   
admin.site.register(Session,SessionsAdmin)   
