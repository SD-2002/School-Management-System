# Generated by Django 4.1.3 on 2022-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0006_rename_roll_no_attendance_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
