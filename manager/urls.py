from django.urls import path
from .views import HomeView
from .views import DisciplinesView
from .views import StudentsView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentsView.as_view(), name='students'),
    path('disciplines/', DisciplinesView.as_view(), name='disciplines'),
]
