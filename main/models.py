from django.db import models

class TodoModel(models.Model):
    task_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Задача: {self.task_name}, описание: {self.desc}, статус: {self.is_completed}'