from django.contrib import admin

from education.models import Instructor, Student

# Register your models here.

admin.site.register(Student)

admin.site.register(Instructor)
