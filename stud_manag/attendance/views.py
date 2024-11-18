from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Student
# from .serializers import StudentSerializer
# from users.permissions import IsStudent, IsAdmin
# from rest_framework.permissions import IsAuthenticated

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get_permissions(self):
#         if self.action in ['retrieve', 'update', 'partial_update']:
#             self.permission_classes = [IsStudent | IsAdmin]
#         else:
#             self.permission_classes = [IsAdmin]
#         return super().get_permissions()

#     def get_queryset(self):
#         if self.request.user.role == 'student':
#             return Student.objects.filter(user=self.request.user)
#         return super().get_queryset()




from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from users.permissions import IsTeacherOrAdmin, IsStudentOrAdmin

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacherOrAdmin]




# Create your views here.
