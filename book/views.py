from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
 
class StudentsList(generics.ListCreateAPIView):
     permission_classes = (IsAuthenticatedOrReadOnly,)

     queryset = Student.objects.all()
     serializer_class = StudentSerializer

class StudentsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Student.objects.all()
    serializer_class = StudentSerializer