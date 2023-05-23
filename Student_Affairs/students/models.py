from operator import truediv
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length=15)
    gpa = models.FloatField()
    level = models.IntegerField()
    birthdate = models.DateField()
    gender = models.CharField(max_length=6)
    dep = models.CharField(max_length= 10,  default='General')
    state = models.BooleanField(default= False)
    
    

class state(models.Model):
    state = models.BooleanField(default= False)
    stateID = models.IntegerField()
    
    def __str__(self):
        return self.state
    
    def __str__(self):
        return self.id
