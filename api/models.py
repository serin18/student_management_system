from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=250)
    description=models.TextField()

class Student_Profile(models.Model):
    full_name=models.CharField(max_length=100)
    reg_number=models.IntegerField(unique=True)
    phone_number=models.IntegerField(null=True)
    email=models.EmailField()
    depart=models.ForeignKey(Department,on_delete=models.CASCADE)

