from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.TextField()
    jobtitle=models.TextField()
    def __str__(self):
        return self.jobtitle
