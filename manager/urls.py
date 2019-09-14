from django.urls import path
from django.conf.urls import url
from .views import HomeView
from .views import DisciplinesListView
from .views import StudentSearchView
from .views import ScheduleView
from .views import student_presence
from .views import SingleDisciplineView
from .views import ClassPresenceView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentSearchView.as_view(), name='students'),
    path('disciplines/', DisciplinesListView.as_view(), name='disciplines'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('students/<int:pk>/', student_presence, name='student_presence'),
    path('disciplines/<int:pk>/', SingleDisciplineView.as_view(), name='single_discipline'),
    path('presence/<int:pk>/', ClassPresenceView.as_view(), name='class_presence'),
]
