"""Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')"""

from django.urls import path
from .views import CourseListView,CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/',CourseDetailView.as_view(), name='course_detail'),
]
