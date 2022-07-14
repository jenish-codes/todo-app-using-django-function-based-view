from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=200)
