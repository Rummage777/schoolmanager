from django.urls import path
from django.conf.urls import url
from .views import HomeView
from .views import DisciplinesListView
from .views import StudentSearchView
from .views import ScheduleView
from .views import student_presence
from .views import class_presence
# from .views import ClassPresenceView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentSearchView.as_view(), name='students'),
    path('disciplines/', DisciplinesListView.as_view(), name='disciplines'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('students/<int:pk>/', student_presence, name='student_presence'),
    path('presence/<int:pk>/', class_presence, name='class_presence'),
    # path('presence/<int:pk>/', ClassPresenceView.class_presence, name='class_presence'),
]
