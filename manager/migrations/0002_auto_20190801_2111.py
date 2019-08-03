# Generated by Django 2.2.3 on 2019-08-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_entrance_date',
            new_name='entrance_date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_exit_date',
            new_name='exit_date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_full_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_userpic_file_name',
            new_name='userpic_file_name',
        ),
        migrations.AddField(
            model_name='presence',
            name='grade_value',
            field=models.CharField(choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Avarage'), ('2', 'Bad')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='knowledge_level',
            field=models.CharField(choices=[('NE', 'Newbie'), ('JR', 'Junior'), ('MD', 'Middle'), ('SR', 'Senior')], default=None, max_length=6),
        ),
        migrations.AddField(
            model_name='student',
            name='student_activity',
            field=models.BooleanField(default=None),
        ),
    ]
