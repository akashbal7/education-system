from django import forms
from .models import CourseInstructor, CustomUser

class CourseInstructorForm(forms.ModelForm):
    class Meta:
        model = CourseInstructor
        fields = ['course', 'instructor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = CustomUser.objects.filter(role='TEACHER')

