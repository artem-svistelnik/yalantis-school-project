from .serializers import CourseSerializer
from .models import Course
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['start_date', 'finish_date']
    search_fields = ['course_title',]
