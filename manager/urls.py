from django.urls import path
from .views import HomeView
from .views import DisciplinesListView
from .views import StudentsListView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentsListView.as_view(), name='students'),
    path('disciplines/', DisciplinesListView.as_view(), name='disciplines'),
]
