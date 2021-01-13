# Generated by Django 3.1.5 on 2021-01-11 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('birthday', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Feeding_ration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('characteristic', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=45)),
                ('birthday', models.CharField(max_length=45)),
                ('marital_status', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Reptile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_temperature', models.CharField(max_length=40)),
                ('hibernation_period', models.TextField(max_length=45, null=True)),
                ('animal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wintering_place', models.CharField(max_length=40)),
                ('date_of_arrival', models.CharField(max_length=20)),
                ('flight_date', models.CharField(max_length=20)),
                ('animal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.habitat_area'),
        ),
        migrations.AddField(
            model_name='animal',
            name='caretaker_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caretaker_id', to='provider.user'),
        ),
        migrations.AddField(
            model_name='animal',
            name='ration_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.feeding_ration'),
        ),
        migrations.AddField(
            model_name='animal',
            name='veterenarian_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='veterenarian_id', to='provider.user'),
        ),
    ]