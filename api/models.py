from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, help_text="Task name")
    is_completed = models.IntegerField()
    created_at = models.DateField(null=True, blank=True)
    status = models.IntegerField()

    def __str__(self):
        return self.name