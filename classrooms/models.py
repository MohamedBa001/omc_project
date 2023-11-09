from django.db import models
from groups.models import Group
from speciality.models import Speciality
from accoounts.models import Professor
from courses.models import Course


class Classroom(models.Model):

    classroom_type = models.CharField(max_length=10)
    classroom_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.classroom_type} {self.classroom_number}'

TIMES = (
 (
     "1" ,"08:30-10:00"
 ),
  (
     "2" ,"10:00-11:30"
 ),
  (
     "3" ,"11:30-13:00"
 ),
  (
     "4" ,"13:00-14:30"
 ),
  (
     "5" ,"14:30-16:00"
 ),
)
TYPES =(
    ("TD","TD"),
    ("TP","TP"),
    ("COUR","COUR"),

)

class Session(models.Model):
    session_time = models.CharField(choices=TIMES , max_length=20)
    session_type = models.CharField(choices=TYPES , max_length=5)
    session_date = models.DateField()
    groupe = models.ForeignKey(Group,on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE) 
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.session_time} {self.session_date} {self.session_type}' 