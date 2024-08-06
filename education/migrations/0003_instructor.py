# Generated by Django 5.0.7 on 2024-08-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(default='12345678', max_length=100)),
            ],
        ),
    ]
