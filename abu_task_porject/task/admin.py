from django.contrib import admin
from .models import TaskModel

# Register your models here.


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('taskTitle', 'taskDescription')


admin.site.register(TaskModel, TaskModelAdmin)
