from .serializers import AvtorsSerializer, BooksSerializer
from rest_framework.views import APIView
from .models import Books, Avtors
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import generics


# Create your views here.
class BooklistALLView(generics.ListAPIView):
    queryset = Avtors.objects.all()
    qweryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDetalesView(generics.RetrieveAPIView):
    queryset = Avtors.objects.all()
    qweryset = Books.objects.all()
    serializer_class = BooksSerializer, AvtorsSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Avtors.objects.all()
    queryset = Books.objects.all()
    serializer_class = BooksSerializer, AvtorsSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Avtors.objects.all()
    qweryset = Books.objects.all()
    serializer_class = BooksSerializer, AvtorsSerializer


class BookDeleteView(generics.DestroyAPIView):
    queryset = Avtors.objects.all()
    qweryset = Books.objects.all()
    serializer_class = BooksSerializer, AvtorsSerializer
