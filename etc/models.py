from django.db import models

# Create your models here.
class msgs(models.Model):
	id=models.AutoField(primary_key='True')
	charge=models.CharField(max_length=255, default="")
	name=models.CharField(max_length=255, default="")
	msg=models.CharField(max_length=1000, default="")
	img=models.FileField(upload_to="media/media/static/", default="")

	def __str__(self):
		return self.name

class faculty(models.Model):
	id=models.AutoField(primary_key='true')
	name=models.CharField(max_length=244, default="")
	appointment=models.CharField(max_length=244, default="")
	desc=models.CharField(max_length=2444, default="")
	contact=models.CharField(max_length=255, default="")
	img=models.FileField(upload_to="media/media/static/", default="")

	def __str__(self):
		return self.name

class news(models.Model):
	id=models.AutoField(primary_key='true')
	date=models.DateField()
	news=models.CharField(max_length=1000, default='')


	def __str__(self):
		return str(self.date)


class Category(models.Model):
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=123, default="")
	def __str__(self):
		return self.title


class courses(models.Model):
	id=models.AutoField(primary_key='true')
	course_name=models.CharField(max_length=255, default='')
	course_desc=models.CharField(max_length=1000, default='')
	photo=models.FileField(upload_to='media/media/static', default="")
	category=models.ForeignKey(Category, on_delete=models.CASCADE, default="")
	date=models.CharField(max_length=255, default='')
	status=models.CharField(max_length=255, default='')
	def __str__(self):
		return self.course_name



	
class photos(models.Model):
	id=models.AutoField(primary_key='true')
	photo=models.FileField(upload_to='media/media/static', default="")
	date=models.DateField(default="")
	def __str__(self):
		return str(self.date)

class messages(models.Model):
	id=models.AutoField(primary_key='true')
	name=models.CharField(max_length=255, default='')
	email=models.CharField(max_length=255, default='')
	text=models.CharField(max_length=1000, default='')
	def __str__(self):
		return self.name
