from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from users.permissions import IsTeacherOrAdmin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Course

@receiver(post_save, sender=Course)
def clear_course_cache(sender, instance, **kwargs):
    cache.delete('course_list_cache_key')

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrAdmin]
    
    def list(self, request, *args, **kwargs):
        cache_key = 'course_list_cache_key'
        cached_courses = cache.get(cache_key)
        if cached_courses:
            return Response(cached_courses)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, 60 * 15)  # Cache for 15 minutes
        return response


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsTeacherOrAdmin]


# Create your views here.
