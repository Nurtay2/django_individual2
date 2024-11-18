from django.shortcuts import render
from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer
from users.permissions import IsTeacherOrAdmin, IsStudentOrAdmin

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsTeacherOrAdmin]



# Create your views here.
