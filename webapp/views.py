from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import userInfo

from .serializers import userInfoSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def webappOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = userInfo.objects.all()
    serializer = userInfoSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks = userInfo.objects.get(id=pk)
    serializer = userInfoSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = userInfoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = userInfo.objects.get(id = pk )
    serializer = userInfoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = userInfo.objects.get(id = pk )
    task.delete()

    return Response("items removed successfully!")