from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
        ('SUPERADMIN', 'Superadmin'),
        ('ADMIN', 'Admin'),
    ]
    # Add your custom fields here
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='STUDENT'
    )

    department = models.CharField(
        max_length=100,
        default='not assigned'
    )

    def __str__(self):
        return self.username

    
    
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True)
    courses = models.IntegerField(default=0)
    semesters = models.IntegerField(default=0)
    course_image = models.ImageField(upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class CourseInstructor(models.Model):
    course = models.ForeignKey(Course, related_name='course_instructors', on_delete=models.CASCADE)
    instructor = models.ForeignKey(CustomUser, related_name='course_instructors', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'instructor'),)
        verbose_name = "CourseInstructor"
        verbose_name_plural = "Assign teacher to course"
    
    def __str__(self):
        return f"{self.course.name} - {self.instructor.username}"
    


class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name} on {self.enrollment_date}"
    
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Assign Students to course"

from django.db import models

class Quote(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
