from django.urls import path
from django.conf.urls import url
from .views import HomeView
from .views import DisciplinesListView
from .views import StudentsListView
from .views import StudentSearchView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentsListView.as_view(), name='students'),
    path('disciplines/', DisciplinesListView.as_view(), name='disciplines'),
    url(r'student_search/', StudentSearchView.as_view(), name='student_search'),
]
