from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class team(models.Model):
    team_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    team_leader_github = models.CharField(max_length=255, blank=False, null=False, unique=True)
    member1_github = models.CharField(max_length=255, blank=True, null=True, unique=True)
    member2_github = models.CharField(max_length=255, blank=True, null=True, unique=True)
    member3_github = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.team_name


class phaseSelectionModel(models.Model):
    team = models.OneToOneField(team, on_delete=models.CASCADE, null=False)
    round = models.IntegerField(default=1, null=False, blank=False)
    def __str__(self):
        return str(self.team)


class manageTeam(models.Model):
    User_CHOICES = [
        ('j', 'judge'),
        ('o', 'organiser'),
        ('m', 'mentor')
    ]

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=False)
    role = models.CharField(max_length=255, choices=User_CHOICES, null=False, blank=False)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=team)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        phaseSelectionModel.objects.create(team=instance)
