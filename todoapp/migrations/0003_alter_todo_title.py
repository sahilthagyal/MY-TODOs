# Generated by Django 5.1.1 on 2025-03-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Title',
            field=models.CharField(max_length=1000),
        ),
    ]
