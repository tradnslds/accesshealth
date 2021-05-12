from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
	Employee_name=models.CharField(max_length=30)
	Department=models.CharField(max_length=30)
	Email=models.CharField(max_length=30)
	# Date_of_birth=models.DateField(defalut=timezone.now())
	Picture=models.CharField(max_length=128)

	def __str__(self):
		return self.Employee_name

class Department(models.Model):
	Department_name=models.CharField(max_length=30)
	Manager=models.CharField(max_length=30)

	def __str__(self):
		return self.Department_name

