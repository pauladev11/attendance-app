from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone



class EmployeeUser(AbstractUser):
    
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24)
    birth_date = models.DateField(blank=True, null=True)
    manager = models.BooleanField(blank=True, default=False, null=True)


    def __str__(self):
        return self.username + ' - ' + self.firstname + ' ' + self.lastname



