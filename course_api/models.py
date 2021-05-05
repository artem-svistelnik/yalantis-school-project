from django.db import models


class Course(models.Model):
    course_title = models.CharField(max_length=255, verbose_name="Course title")
    start_date = models.DateField(verbose_name="Course start date")
    finish_date = models.DateField(verbose_name="Course finish date")
    lectures_count = models.PositiveIntegerField(verbose_name="Count of lectures")

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["id"]
