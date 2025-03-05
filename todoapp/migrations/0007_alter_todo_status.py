# Generated by Django 5.1.1 on 2025-03-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('1', 'Completed'), ('2', 'Active'), ('3', 'Has due date')], default='3', max_length=100),
        ),
    ]
