# Generated by Django 3.1.5 on 2021-01-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20210112_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='Cost_per_minute',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='Cost_per_minute_from_2am_to_6am',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='Cost_per_minute_from_8pm_to_2am',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='Number_of_minutes_of_session',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='Total_cost',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]