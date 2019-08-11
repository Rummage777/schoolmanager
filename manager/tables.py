import django_tables2 as tables
from .models import Discipline, Student


class DisciplineTable(tables.Table):
    class Meta:
        model = Discipline


class StudentTable(tables.Table):
    class Meta:
        model = Student

