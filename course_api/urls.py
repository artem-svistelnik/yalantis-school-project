from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "course_api"


router = routers.DefaultRouter()
router.register(r"courses", views.CourseView)
urlpatterns = [
    path("", include(router.urls)),
]
