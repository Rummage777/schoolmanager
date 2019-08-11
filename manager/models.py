from django.db import models
import datetime


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    entrance_date = models.DateField(null=True)
    exit_date = models.DateField(blank=True, null=True)
    knowledge_level_choices = [
        ('NE', 'Newbie'),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    ]

    knowledge_level = models.CharField(max_length=6, choices=knowledge_level_choices, default=None)
    userpic_file_name = models.CharField(max_length=200, blank=True, null=True)

    student_activity = models.BooleanField(default=None)

    def __str__(self):
        return self.full_name


    def update_student_activity(self):
        '''Returns the student activity status: True or False'''
        today = datetime.date.today()
        if self.entrance_date < today and (self.exit_date is None or today < self.exit_date):
            self.student_activity = True
        else:
            self.student_activity = False
        self.save()


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=200)

    def __str__(self):
       return self.discipline_name


class Schedule(models.Model):
    discipline = models.ForeignKey(Discipline, models.PROTECT)
    class_dt = models.DateTimeField()

    def __str__(self):
        return '{} ({:%d.%m.%Y %H:%M})'.format(self.discipline.discipline_name, self.class_dt)


class Presence(models.Model):
    schedule = models.ForeignKey(Schedule, models.PROTECT)
    student = models.ForeignKey(Student, models.PROTECT)
    grade_value_choices = [
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Avarage'),
        ('2', 'Bad'),
    ]
    grade_value = models.CharField(max_length=10, choices=grade_value_choices, default=None)

    def __str__(self):
        return self.schedule.discipline.discipline_name
