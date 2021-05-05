from django.urls import path,include
from . import views
from rest_framework import routers

app_name='course_api'


router = routers.DefaultRouter()
router.register(r'courses', views.CourseView)
urlpatterns = [
    path('', include(router.urls)),
]
