# Generated by Django 3.0.4 on 2020-04-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complexModules', '0003_auto_20200404_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='roundDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('round_todo', models.TextField()),
                ('round_info', models.TextField()),
                ('round_template', models.TextField()),
            ],
        ),
    ]
