from django.db import models

class Speciality(models.Model):
     
     user = models.ForeignKey('accoounts.CustomUser',on_delete=models.CASCADE)
     speciality_name = models.CharField(max_length=100)
     speciality_code = models.CharField(max_length=20,unique=True) 

     def __str__(self):
        return self.speciality_name
     