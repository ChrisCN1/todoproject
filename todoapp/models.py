from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} | {self.description} | {self.due_date}'

