from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name',
                    'last_name','identification_number')
    search_fields = ('first_name','middle_name',
                    'last_name','identification_number')

admin.site.register(Student,StudentAdmin)

