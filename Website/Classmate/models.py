from django.db import models
import datetime
from django.utils import timezone


class Course(models.Model):
    Course_name = models.CharField(max_length=500)
    Courses_id = models.CharField(max_length=500)
    started_from = models.DateTimeField('Started from')
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.Course_name

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.started_from <= now


class Details(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    Duration = models.CharField(max_length=500)
    Course_type = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.Course_type


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
