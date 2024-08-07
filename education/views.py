from django.shortcuts import render, redirect

from education.models import Course, CustomUser, Quote   

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

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
        return redirect('/')
    else:
        
        return render(request, 'contact.html')



