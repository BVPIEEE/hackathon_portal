from django.db import models


# Create your models here.
class scoringModel(models.Model):
    scoringNumber = models.IntegerField(null=False, blank=False)
    client = models.CharField(max_length=1000, null=True, blank=True)
    api_key = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.scoringNumber)
