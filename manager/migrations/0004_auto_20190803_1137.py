# Generated by Django 2.2.3 on 2019-08-03 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20190803_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.Discipline', verbose_name='Занятие'),
        ),
    ]
