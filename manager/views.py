from django.views.generic.base import TemplateView
from .models import Discipline
from .models import Student
from django.views.generic import ListView
from django.db.models import Q

# My pages views here

class HomeView(TemplateView):

    template_name = 'home.html'


class StudentsListView(TemplateView):

    template_name = 'students.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.order_by('full_name', 'entrance_date')
        return context


class StudentSearchView(ListView):
    model = Student

    # Use this template for filtering student list on the same page Student
    template_name = 'students.html'

    # Use this template for showing search result on separate page  Search results
    # template_name = 'search_result.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(Q(full_name__icontains=q))
        return queryset


class DisciplinesListView(TemplateView):

    template_name = 'disciplines.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discipline_list'] = Discipline.objects.all()
        return context

