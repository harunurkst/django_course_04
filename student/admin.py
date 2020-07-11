from django.contrib import admin
from .models import StudentList


class StudentListAdmin(admin.ModelAdmin):
    list_display = ['roll', 'name', 'std_class', 'gender']
    list_editable = ['name', 'gender']


admin.site.register(StudentList, StudentListAdmin)
