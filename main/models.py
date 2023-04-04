from django.db import models

class TodoModel(models.Model):
    task = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)

    is_completed = models.BooleanField(default=False)
