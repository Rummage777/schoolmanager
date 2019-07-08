from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


'''
CREATE TABLE STUDENTS (
    "student_id" serial NOT NULL PRIMARY KEY,
    "student_full_name" varchar(255) NOT NULL,
    "student_entrance_date"  NOT NULL,
    "student_exit_date" NOT NULL,
    "student_knowledge_level" varchar(255) NOT NULL,
    "student_userpic_file_name" varchar(255) NOT NULL,
    "student_status" NOT NULL,
);
'''


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_full_name = models.CharField(max_length=200)
    student_entrance_date = models.DateField()
    student_exit_date = models.DateField(blank=True, null=True)
    student_knowledge_level = [
        ('NE', 'Newbie'),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    ]
    student_userpic_file_name = models.CharField(max_length=200, blank=True, null=True)

    def student_status(self):
        '''Returns the student activity status:
         ('0', 'Inactive'),
         ('1', 'Active')"
        '''

        if self.student_entrance_date < today.datetime and (self.student_exit_date == Null or today.datetime < self.student_exit_date):
            return 0
        else:
            return 1


class Discipline_list(models.Model):
    discipline_id = models.AutoField(primary_key=True)
    discipline_name = models.CharField(max_length=200)


class Classes_schedule(models.Model):
    class_id = models.AutoField(primary_key=True)
    discipline = models.ForeignKey(Discipline_list, on_delete=models.CASCADE)
    class_date = models.DateField()
    class_time = models.TimeField()
    marks = models.ForeignKey(Presence_and_grades, on_delete=models.CASCADE)


class Presence_and_grades(models.Model):
    marks_id = models.AutoField(primary_key=True)
    current_class = models.ForeignKey(Classes_schedule, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    presence_mark = models.IntegerField()
    grade_value = [
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Avarage'),
        ('2', 'Bad'),
    ]

