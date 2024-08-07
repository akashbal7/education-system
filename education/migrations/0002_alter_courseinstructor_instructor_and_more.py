# Generated by Django 5.0.7 on 2024-08-07 01:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstructor',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instructors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default='not assigned', max_length=100),
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
