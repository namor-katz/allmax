from django.shortcuts import render
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def index(request):
    '''this is base view'''
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


@api_view(['GET', 'POST'])
def api_tasks(request):
    ''' this is list tasks return'''
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks,  many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'PATH', 'DELETE'])
def api_task_detail(request, pk):
    ''' return detail tasks'''
    task = Tasks.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    elif request.method == "PUT" or request.method == "PATCH":
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_201_NO_CONTENT)
