from django.contrib import admin

from education.models import Course, CourseInstructor, Enrollment, Instructor, Student

# Register your models here.

admin.site.register(Student)

admin.site.register(Instructor)

admin.site.register(Course)

admin.site.register(CourseInstructor)

admin.site.register(Enrollment)
