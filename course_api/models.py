from django.db import models

# Create your models here.
class Course(models.Model):
    course_title=models.CharField(max_length=255,verbose_name='Название курса')
    start_date=models.DateField(verbose_name='Дата начала курса')
    finish_date=models.DateField(verbose_name='Дата завершения курса')
    lectures_count=models.PositiveIntegerField(verbose_name='Количество лекций')

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'
        ordering = ['id']
