from django.db import models

# Create your models here.
class Experience(models.Model):
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.TextField()
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()