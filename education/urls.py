from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='index'),     
     path('blog/', views.blog, name='blog'),
     path('about/', views.about, name='about'),
     path('course/', views.course, name='course-grid-2'),
     path('teachers/', views.teachers, name='teachers'),
]