from django.urls import path
from .views import HomeTemplate
from .views import DisciplinesTemplate
from .views import StudentsTemplate



urlpatterns = [
    path('', HomeTemplate.as_view(), name='home'),
    path('students/', StudentsTemplate.as_view(), name='students'),
    path('disciplines/', DisciplinesTemplate.as_view(), name='disciplines'),
]
