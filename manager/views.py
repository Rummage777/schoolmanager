from django.views.generic.base import TemplateView
from .models import Discipline
from .models import Student
from .models import Schedule
from .models import Presence
from django.views.generic import ListView
from django.db.models import Q

# My pages views here

class HomeView(TemplateView):

    template_name = 'home.html'

class StudentSearchView(ListView):
    model = Student

    # Use this template for filtering student list on the same page Student
    template_name = 'students.html'

    # Use this template for showing search result on separate page  Search results
    # template_name = 'search_result.html'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('full_name', 'entrance_date')
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

class ScheduleView(ListView):
    model = Schedule

    # Use this template for filtering student list on the same page Student
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_schedule'] = Schedule.objects.all().order_by('class_dt', 'discipline')
        return context

class StudentPresenceView(ListView):
    model = Presence

    template_name = 'studentpresence.html'

    def student_presence(request, pk):
        post = get_object_or_404(Student, pk=pk)
        return render(request, {'student': student})

class ClassPresenceView(ListView):
    model = Presence

    template_name = 'classpresence.html'

    def class_presence(request, pk):
        post = get_object_or_404(Discipline, pk=pk)
        return render(request, {'class': class})

