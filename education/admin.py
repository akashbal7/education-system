from click import Group
from django.contrib import admin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from education.models import Blog, Course, CourseInstructor, CustomUser, Enrollment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'department')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'department', 'is_active', 'is_staff')

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
    
    
# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser

    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'department', 'isLogin')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'department', 'isLogin')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Course)

admin.site.register(CourseInstructor)

admin.site.register(Enrollment)

admin.site.register(Blog)

