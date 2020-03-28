from django.test import TestCase
from django.utils import timezone
from .models import Course
# Create your tests here.
class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
             title ="Clean Code",
             description="Learn how to write readable code"
             "")
        now = timezone.now()
        self.assertLess(course.created_at,now)

class CourseViewTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
                      title = "Adobe PhotoShop 2021",
                      description = "Become a 21 st Graphic Designer"
        )
        self.course2 = Course.objects.create(
                      title = "Adobe Indesign 2021",
                      description = "Become a 21 st Graphic Designer"
        )




