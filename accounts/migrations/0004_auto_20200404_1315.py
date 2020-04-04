# Generated by Django 3.0.4 on 2020-04-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200402_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phaseselectionmodel',
            name='final',
        ),
        migrations.RemoveField(
            model_name='phaseselectionmodel',
            name='section1',
        ),
        migrations.RemoveField(
            model_name='phaseselectionmodel',
            name='section2',
        ),
        migrations.RemoveField(
            model_name='phaseselectionmodel',
            name='section3',
        ),
        migrations.RemoveField(
            model_name='phaseselectionmodel',
            name='section4',
        ),
        migrations.AddField(
            model_name='phaseselectionmodel',
            name='round',
            field=models.IntegerField(default=1),
        ),
    ]