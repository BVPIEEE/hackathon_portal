from django.db import models


# Create your models here.
class scoringModel(models.Model):
    client = models.CharField(max_length=1000, null=True, blank=True)
    api_key = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.client)

class submissionModel(models.Model):
    sheet_id = models.TextField(null = False, blank=False)
    round = models.IntegerField(null=False, blank=False)
    state_column = models.CharField(max_length=255, null=False, blank=False)
    form_link = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.round)

class gradeModel(models.Model):
    sheet_id = models.TextField(null = False, blank=False)
    round = models.IntegerField(null=False, blank=False)
    state_column = models.CharField(max_length=255, null=True, blank=True)
    form_link = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.round)
            
class currentRound(models.Model):
    round = models.IntegerField(null=False, blank=False)