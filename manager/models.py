from django.db import models
import datetime


class Student(models.Model):
    student_full_name = models.CharField(max_length=200)
    student_entrance_date = models.DateField(null=True)
    student_exit_date = models.DateField(blank=True, null=True)
    student_knowledge_level = [
        ('NE', 'Newbie'),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    ]
    student_userpic_file_name = models.CharField(max_length=200, blank=True, null=True)

    def is_active(self):
        '''Returns the student activity status:
         ('0', 'Inactive'),
         ('1', 'Active')"
        '''

        return self.student_entrance_date < today.datetime and (self.student_exit_date == Null or today.datetime < self.student_exit_date)


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=200)


class Schedule(models.Model):
    discipline_id = models.ForeignKey(Discipline, models.PROTECT)
    class_dt = models.DateTimeField()


class Presence(models.Model):
    schedule_id = models.ForeignKey(Schedule, models.PROTECT)
    student_id = models.ForeignKey(Student, models.PROTECT)
    grade_value = [
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Avarage'),
        ('2', 'Bad'),
    ]

