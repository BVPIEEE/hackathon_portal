from django.contrib.auth.models import AbstractUser
from django.db import models


class team(models.Model):
    team_name = models.CharField(max_length=255, blank=False, null=False)
    team_leader_github = models.CharField(max_length=255, blank=False, null=False)
    team_leader_email = models.CharField(max_length=255, blank=False, null=False)
    member1_github = models.CharField(max_length=255, blank=False, null=False)
    member1_email = models.CharField(max_length=255, blank=False, null=False)
    member2_github = models.CharField(max_length=255, blank=True, null=True)
    member2_email = models.CharField(max_length=255, blank=True, null=True)
    member3_github = models.CharField(max_length=255, blank=True, null=True)
    member3_email = models.CharField(max_length=255, blank=True, null=True)
    member4_github = models.CharField(max_length=255, blank=True, null=True)
    member4_email = models.CharField(max_length=255, blank=True, null=True)


class phaseSelectionModel(models.Model):
    team = models.OneToOneField(team, on_delete=models.CASCADE, null=False)
    section1 = models.BooleanField(default=True)
    section2 = models.BooleanField(default=False)
    section3 = models.BooleanField(default=False)
    section4 = models.BooleanField(default=False)
    final = models.BooleanField(default=False)
