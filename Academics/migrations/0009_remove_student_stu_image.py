# Generated by Django 4.1.3 on 2022-11-30 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0008_alter_mark_semester_alter_mark_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_image',
        ),
    ]
