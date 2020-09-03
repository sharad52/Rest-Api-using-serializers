from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import userInfo
from .serializers import userInfoSerializer

# Create your views here.
class userList(APIView):
    def get(self,request):
        user = userInfo.objects.all()
        serializer = userInfoSerializer(user,many=True)
        return Response(serializer.data)

    def post(self):
        pass