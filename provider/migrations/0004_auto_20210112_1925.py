# Generated by Django 3.1.5 on 2021-01-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_auto_20210112_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='Price_Cost_per_minute',
            new_name='Cost_per_minute',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='Operator_Employee_ID',
            new_name='Employee_ID',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='Receipt_shift_number',
            new_name='Shift_number',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Price_Cost_per_minute',
            new_name='Cost_per_minute',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Operator_Employee_ID',
            new_name='Employee_ID',
        ),
    ]
