from django.contrib import admin

# Register your models here.
from .models import Course

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('id','course_title')
