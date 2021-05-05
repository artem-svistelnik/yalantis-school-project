from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Course



class CourseApiTest(APITestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            course_title="title",
            start_date="2021-05-05",
            finish_date="2021-05-30",
            lectures_count=15,
        )

    def test_course_list_get_request(self):
        url = "/api/courses/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, "objects not found")

    def test_course_get_request(self):
        url = "/api/courses/{}/".format(self.course.id)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "course_title": "title",
                "start_date": "2021-05-05",
                "finish_date": "2021-05-30",
                "lectures_count": 15,
            },
            "object not found",
        )

    def test_course_post_request(self):
        url = "/api/courses/"
        data = {
            "course_title": "new title",
            "start_date": "2021-05-04",
            "finish_date": "2021-05-21",
            "lectures_count": 15,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            {
                "id": 2,
                "course_title": "new title",
                "start_date": "2021-05-04",
                "finish_date": "2021-05-21",
                "lectures_count": 15,
            },
            "object not created",
        )
        self.assertEqual(Course.objects.count(), 2, "object not created")
        self.assertEqual(
            Course.objects.get(id=2).course_title, "new title", "object not created"
        )

    def test_course_put_request(self):
        url = "/api/courses/{}/".format(self.course.id)
        data = {
            "course_title": "change title",
            "start_date": "2021-05-04",
            "finish_date": "2021-05-21",
            "lectures_count": 20,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, "object not changed")
        self.assertEqual(
            Course.objects.get(id=1).course_title, "change title", "object not changed"
        )

    def test_course_delete_request(self):
        url = "/api/courses/{}/".format(self.course.id)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, "object not deleted"
        )
        self.assertNotIn(self.course, Course.objects.all(), "object not deleted")

    def test_get_request_filter(self):
        url = "/api/courses/?start_date=05.05.2021&finish_date=30.05.2021"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, "request error")

    def test_get_request_search(self):
        url = "/api/courses/?search=title"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, "request error")


class CourseApiFailedTest(APITestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            course_title="title",
            start_date="2021-05-05",
            finish_date="2021-05-30",
            lectures_count=15,
        )

    def test_course_get_request(self):
        url = "/api/courses/777/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND,'object found')

    def test_course_post_request(self):
        url = "/api/courses/"
        data = {
            "course_title": "new title",
            "start_date": "2021-05-04",
            "finish_date": "2021-05-21",
            "lectures_count": 'asf',
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST,'object create')

    def test_course_put_request(self):
        url = "/api/courses/{}/".format(self.course.id)
        data = {
            "course_title":"change title",
            "start_date": "2021.05.04",
            "finish_date": "2021-05-21",
            "lectures_count": 20,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "object changed")

    def test_course_delete_request(self):
        url = "/api/courses/777/"
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND, "object not deleted"
        )
        self.assertIn(self.course, Course.objects.all(), "object not deleted")

    def test_get_request_filter(self):
        url = "/api/courses/?start_date=05.05.2021&finish_date=30-05-2021"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "request 200 ok")

