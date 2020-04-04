# Generated by Django 3.0.4 on 2020-04-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200402_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member1_github',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='member2_github',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='member3_github',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_leader_github',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
