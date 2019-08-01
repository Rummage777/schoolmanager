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

    def update_student_activity(activity):
        '''Returns the student activity status: True or False'''
        if self.entrance_date < today.datetime and (self.exit_date == Null or today.datetime < self.exit_date):
            activity.student_activity = True
        else:
            activity.student_activity = False
        activity.save()


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=200)


class Schedule(models.Model):
    discipline_id = models.ForeignKey(Discipline, models.PROTECT)
    class_dt = models.DateTimeField()


class Presence(models.Model):
    schedule_id = models.ForeignKey(Schedule, models.PROTECT)
    student_id = models.ForeignKey(Student, models.PROTECT)
    grade_value_choices = [
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Avarage'),
        ('2', 'Bad'),
    ]
    grade_value = models.CharField(max_length=10, choices=grade_value_choices, default=None)


