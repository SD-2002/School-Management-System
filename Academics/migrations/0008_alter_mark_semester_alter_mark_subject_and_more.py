# Generated by Django 4.1.3 on 2022-11-30 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0007_alter_student_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='Semester',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mark',
            name='Subject',
            field=models.CharField(max_length=19),
        ),
        migrations.AlterField(
            model_name='mark',
            name='Year',
            field=models.CharField(max_length=20),
        ),
    ]
