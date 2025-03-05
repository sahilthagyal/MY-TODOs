# Generated by Django 5.1.1 on 2025-03-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('1', 'All'), ('2', 'Completed'), ('3', 'Active'), ('4', 'Has due date')], default='3', max_length=100),
        ),
    ]
