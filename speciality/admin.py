from django.contrib import admin
from .models import Speciality

class SpecialityAdmin(admin.ModelAdmin):
    list_display =("user","speciality_code","speciality_name")
admin.site.register(Speciality,SpecialityAdmin)
 
