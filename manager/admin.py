from django.contrib import admin
from .models import Student
from .models import Discipline
from .models import Schedule
from .models import Presence

admin.site.register(Student)
admin.site.register(Discipline)
admin.site.register(Schedule)
admin.site.register(Presence)

