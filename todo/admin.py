from django.contrib import admin
from .models import Tasks

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_create',  'target_user')
    search_fields = ('title', 'target_user')

admin.site.register(Tasks, TasksAdmin)
