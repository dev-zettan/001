from django.shortcuts import render

# Create your views here.


from .models import Task01, Task02, Task03
from django.contrib.auth.models import User

from .serializer import Task01Serializer, Task02Serializer, Task03Serializer

from rest_framework import generics
from rest_framework import viewsets


class Task01ViewSet(viewsets.ModelViewSet):
    queryset = Task01.objects.all()
    serializer_class = Task01Serializer


# class Task01RetrieveView(viewsets.ModelViewSet):


class Task02ListView(generics.ListAPIView):
    queryset = Task02.objects.all()
    serializer_class = Task02Serializer


class Task02CreateView(generics.CreateAPIView):
    queryset = Task02.objects.all()
    serializer_class = Task02Serializer


class Task03view(generics.ListCreateAPIView):
    queryset = Task03.objects.all()
    serializer_class = Task03Serializer

