from django.contrib import admin
from .models import TodoModel
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Название задачи', {'fields':['task']}],
        ['Описание задачи', {'fields':['desc']}],
        ['Статус', {'fields':['is_completed']}]
    ]

admin.site.register(TodoModel, TodoAdmin)