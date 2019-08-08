from django.contrib import admin
from .models import Tasks

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_create')
    search_fields = ('name', 'target_user')

admin.site.register(Tasks, TasksAdmin)
