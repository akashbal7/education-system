from django.contrib import admin

from education.models import Course, CourseInstructor, CustomUser, Enrollment

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Course)

admin.site.register(CourseInstructor)

admin.site.register(Enrollment)

