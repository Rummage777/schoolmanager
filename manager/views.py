from django.views.generic.base import TemplateView
from .models import Discipline
from .models import Student


# My pages views here

class HomeView(TemplateView):

    template_name = 'home.html'


class StudentsListView(TemplateView):

    template_name = 'students.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        return context


class DisciplinesListView(TemplateView):

    template_name = 'disciplines.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discipline_list'] = Discipline.objects.all()
        return context

