from django.db import models
from employee.models import EmployeeUser
from django.utils import timezone

class Attendance(models.Model):
    employeeuser = models.ForeignKey(EmployeeUser, on_delete=models.CASCADE, related_name='employeeusers')
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.firstname} {self.employee.lastname} - In: {self.time_in}, Out: {self.time_out or '---'}"
