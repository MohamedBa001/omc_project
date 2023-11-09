from django.db import models
from speciality.models import Speciality

class Course(models.Model):

 course_name = models.CharField(max_length=100)
 course_code = models.CharField(max_length=100,unique=True)
 speciality = models.ForeignKey(Speciality,verbose_name=("course code"), on_delete=models.CASCADE)

 def __str__(self):
    return f'{self.course_code}'
