from django.http import HttpResponse
from django.shortcuts import render
import gradio as gr

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def teachers(request):
    return render(request, 'teachers.html')

def course(request):
    return render(request, 'cours-grid-2.html')