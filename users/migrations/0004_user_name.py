# Generated by Django 5.1.7 on 2025-03-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_classtag_subject_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='any_name', max_length=255),
            preserve_default=False,
        ),
    ]
