from django.contrib import admin
from django.urls import path, include
from etc  import views
urlpatterns = [
	path('etc/', views.index, name='home'),
	path('courses', views.course_func, name='courses'),
	path('gallery', views.gallery, name='gallery'),
	path('contactus', views.contactus, name="contactus"),
	path('faculty', views.facultyfunc, name='facultypage'),
	path("facultyinfo", views.facultyinfo, name="facultyinfo")
]
