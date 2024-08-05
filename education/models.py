from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name
    
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, default='12345678')  # Default password field

    def __str__(self):
        return self.name