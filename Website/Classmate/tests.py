from django.test import TestCase
import datetime
from django.utils import timezone
from.models import Course


class CourseModelTests(TestCase):

    def test_published_recently_with_future_course(self):
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Course(started_from=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_old_course(self):
        time=timezone.now()-datetime.timedelta(days=1,seconds=1)
        old_course=Course(started_from=time)
        self.assertIs(old_course.published_recently(), False)

    def test_published_recently_with_recent_course(self):
        time=timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_course=Course(started_from=time)
        self.assertIs(recent_course.published_recently(), True)
