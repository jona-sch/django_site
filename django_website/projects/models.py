from django.db import models

# Model that tepresents a project
# Attributes:
#     title: CharField[100]
#     description: TextField
#     technology: CHarField[20]
#     image: FilePathField
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="projects/static/img/")
