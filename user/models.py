from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Person(AbstractUser):
	options = (('Female','Female'),('Male','Male'),('NA','Not Specified'))
	username		= models.CharField(max_length=30,unique=True)
	password		= models.CharField(max_length=100)
	email			= models.EmailField(unique=True)
	phone			= models.IntegerField(unique=True,blank=True,null=True)
	first_name 		= models.CharField(max_length=30)
	last_name 		= models.CharField(max_length=30)
	gender			= models.CharField(max_length=30,choices=options)
	address			= models.CharField(max_length=255,default='Sample address')
	pic				= models.ImageField()



	def __str__(self):
  		return self.first_name + ' ' + self.last_name

	