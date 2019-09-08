from django.urls import path
from django.conf.urls import url
from .views import HomeView
from .views import DisciplinesListView
from .views import StudentSearchView
from .views import ScheduleView
from .views import StudentPresenceView
from .views import ClassPresenceView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentSearchView.as_view(), name='students'),
    path('disciplines/', DisciplinesListView.as_view(), name='disciplines'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('students/<int:pk>/', StudentPresenceView.as_view(), name='student_presence'),
    path('presence/<int:pk>/', ClassPresenceView.as_view(), name='class_presence'),
]
