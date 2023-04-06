from django.db import models
from django.contrib.auth.models import User
class TodoModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    task_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Задача: {self.task_name}, описание: {self.desc}, статус: {self.is_completed}'