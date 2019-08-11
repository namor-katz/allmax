from django.shortcuts import render
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    '''this is base view'''
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


@api_view(['GET'])
def api_tasks(request):
    ''' this is list tasks return'''
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks,  many=True)
        return Response(serializer.data)
