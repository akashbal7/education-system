from django.http import HttpResponse
from django.shortcuts import render

from education.models import Course, Instructor

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def teachers(request):
    instructors = Instructor.objects.all()
    return render(request, 'teachers.html', {'instructors': instructors})

def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')