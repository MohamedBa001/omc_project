from django.db import models
from speciality.models import Speciality

class Group(models.Model):
    speciality = models.ForeignKey(Speciality,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id)+":"+self.speciality.speciality_code

