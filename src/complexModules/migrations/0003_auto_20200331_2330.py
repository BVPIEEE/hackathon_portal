# Generated by Django 3.0.4 on 2020-03-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complexModules', '0002_auto_20200331_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoringmodel',
            name='api_key',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='scoringmodel',
            name='client',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
