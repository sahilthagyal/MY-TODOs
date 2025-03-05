from django.contrib import admin
from todoapp.models import todo

# Register your models here.
class todoadmin(admin.ModelAdmin):
    list_display = ('Title','date','status')
admin.site.register(todo,todoadmin)
