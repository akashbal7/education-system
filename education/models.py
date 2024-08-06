from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=128, null=False)
    profile_picture = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, default='12345678')  # Default password field
    profile_picture = models.ImageField(upload_to='instructors/', null=True, blank=True)

    def __str__(self):
        return self.name
    
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
    instructor = models.ForeignKey(Instructor, related_name='course_instructors', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'instructor'),)
        verbose_name = "CourseInstructor"
        verbose_name_plural = "Assign teacher to course"
    
    def __str__(self):
        return f"{self.course.name} - {self.instructor.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name} on {self.enrollment_date}"
    
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Assign Students to course"