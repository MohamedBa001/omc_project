from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
from speciality.models import Speciality 
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)


GENDER_CHOICES = [
    ("M", "male"),
    ("F", "female"),
]
USER_TYPES = [
    ("Professor", "P"),
    ("Student", "S"),
]

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email", unique=True)
    first_name = models.CharField("first name", max_length=200, blank=True)
    last_name = models.CharField("last name", max_length=200, blank=True)
    phone = models.CharField(max_length=12)
    user_type = models.CharField(choices= USER_TYPES, max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("active", default=True)
    is_staff = models.BooleanField("is staff", default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

    def __str__(self):
        return self.get_full_name()   
class Student(models.Model):
   user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
   date_of_birth= models.DateField()
   year_of_study = models.PositiveIntegerField()
   group = models.ForeignKey(Group,on_delete=models.CASCADE)
   speciality=models.ForeignKey(Speciality,on_delete=models.CASCADE)

   def get_full_name(self):
      return self.user.first_name + ' ' + self.user.last_name 
   
   def __str__(self) -> str:
      return self.get_full_name()
   
class Professor(models.Model):
   user = models.OneToOneField(CustomUser,on_delete=models.CASCADE) 
   date_of_birth= models.DateField()
   year_of_teaching = models.PositiveIntegerField()
   group = models.ManyToManyField(Group)
   
   
   def get_full_name(self):
      return self.user.first_name + ' ' + self.user.last_name 
  
   def __str__(self) -> str:
      return self.get_full_name()
########################################################################
