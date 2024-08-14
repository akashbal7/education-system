from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from education.models import Blog, Course, CustomUser, Quote   

# Create your views here.
def home(request):
    instructorCount = CustomUser.objects.filter(role='TEACHER').count
    studentCount = CustomUser.objects.filter(role='STUDENT').count
    totalCourse = Course.objects.all().count
    context = {
        'instructorCount': instructorCount,
        'studentCount': studentCount,
        'totalCourse': totalCourse,
    }
    return render(request, 'index.html', context)

def blog(request):
    blogs = Blog.objects.all
    return render(request, 'blog.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def teachers(request):
    instructors = CustomUser.objects.filter(role='TEACHER')
    return render(request, 'teachers.html', {'instructors': instructors})

def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        details = request.POST.get('comments')

        quote = Quote.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, details=details)
        quote.save()
        print('quote created')
        messages.success(request, 'Quote created successfully!')
        return redirect('contact')
    else:
        
        return render(request, 'contact.html')
    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None :
            user = CustomUser.objects.get(username=username)
            user.isLogin = True
            user.save()
            messages.success(request, 'User logged in successfully')
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Inavlid credentials')
            return render(request, 'login.html')
    else :
        return render(request, 'login.html')


