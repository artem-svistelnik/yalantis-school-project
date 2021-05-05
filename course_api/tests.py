from django.test import TestCase
from .models import Course
from rest_framework.test import APITestCase
from rest_framework import status


class CourseTestCases(TestCase):
    def setUp(self) -> None:
        self.course=Course.objects.create(course_title='title',
                                          start_date='2021-05-05',
                                          finish_date='2021-05-30',
                                          lectures_count=15)
    def is_positive_integer(self,num):
        if num>0 and type(num) is int :
            return True
        else:return False

    def test_add_course(self):
        self.assertIn(self.course,Course.objects.all())
        self.assertTrue(self.is_positive_integer(self.course.lectures_count),"Number is not Positive Integer Type")


class CourseApiTest(APITestCase):
    def setUp(self) -> None:
        self.course=Course.objects.create(course_title='title',
                                          start_date='2021-05-05',
                                          finish_date='2021-05-30',
                                          lectures_count=15)

    def test_course_get_request(self):
        url='/api/courses/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_post_request(self):
        url = '/api/courses/'
        data = {"course_title": "new title",
                "start_date": "2021-05-04",
                "finish_date": "2021-05-21",
                "lectures_count": 15}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_put_request(self):
        url = '/api/courses/{}/'.format(self.course.id)
        data = {"course_title": "change title",
                "start_date": "2021-05-04",
                "finish_date": "2021-05-21",
                "lectures_count": 20}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_delete_request(self):
        url = '/api/courses/{}/'.format(self.course.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
