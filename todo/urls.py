from django.urls import path
from .views import api_tasks

urlpatterns = [
    path('api/tasks/', api_tasks)
]
