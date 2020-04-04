from django.db import models

# Create your models here.
class youtubeModel(models.Model):
    link = models.TextField(blank=False)