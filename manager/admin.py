from django.contrib import admin
from .models import Student
from .models import Discipline
from .models import Schedule
from .models import Presence


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'entrance_date', 'exit_date', 'knowledge_level', 'student_activity')
    list_display_links = ('full_name', 'knowledge_level',)
    list_filter = ('full_name', 'knowledge_level')

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('discipline_name',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'class_dt')
    list_display_links = ('discipline',)

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'student', 'grade_value')
    list_filter = ('schedule', 'student', 'grade_value')
