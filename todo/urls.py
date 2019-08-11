from django.urls import path
from .views import api_tasks, api_task_detail

urlpatterns = [
    path('api/tasks/', api_tasks),
    path('api/tasks/<int:pk>/', api_task_detail)
]
