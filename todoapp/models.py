from django.db import models

# Create your models here.

class todo(models.Model):
    STATUS_CHOICES = [
        ('1', 'Completed'),
        ('2', 'Active'),
        ('3', 'Has due date'),
    ]
    Title = models.CharField(max_length=100)
    date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='3') 


