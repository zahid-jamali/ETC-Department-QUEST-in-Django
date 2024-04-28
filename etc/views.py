from django.shortcuts import render, HttpResponse
from .models import msgs, news, courses, photos, messages, faculty, Category
# Create your views here.
def index(request):
	obj=msgs.objects.all().order_by('-id').values()
	newses=news.objects.all().order_by('-id').values()
	return render(request, "index.html", {'data':obj, 'news': newses,})

def facultyinfo(request):

	Id=request.GET.get("id")
	fac=faculty.objects.filter(id=Id)
	return render(request, "facultyinfo.html", {'fac':fac})


def course_func(request):
	course=courses.objects.all()
	return render(request, 'courses.html', {'courses':course})

def gallery(request):
	pics=photos.objects.all().order_by('-id').values()
	return render(request, 'gallery.html', {'pics':pics})

def facultyfunc(request):
	data=faculty.objects.all()
	return render(request, 'faculty.html', {'data': data} )

def contactus(request):
	if(request.method=='POST'):
		name=request.POST.get('name')
		email=request.POST.get('email')
		text=request.POST.get('text')
		obj=messages()
		obj.name=name
		obj.email=email
		obj.text=text
		obj.save()
	return render(request, 'contactus.html')
