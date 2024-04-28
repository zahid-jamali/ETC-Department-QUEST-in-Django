from django.contrib import admin
from .models import msgs, news, courses, photos, messages, faculty, Category
# Register your models here.
admin.site.register(msgs)
admin.site.register(news)
admin.site.register(courses)
admin.site.register(photos)
admin.site.register(messages)
admin.site.register(faculty)
admin.site.register(Category)
