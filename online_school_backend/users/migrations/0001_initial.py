# Generated by Django 4.1.5 on 2023-02-02 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('father_name', models.CharField(help_text="user's father name", max_length=100)),
                ('mother_name', models.CharField(help_text="user's mother name ", max_length=100)),
                ('date_of_birth', models.DateField(auto_now_add=True, help_text="user's date of birth")),
                ('phone_no', models.IntegerField(help_text="user's phone number")),
                ('user_type', models.CharField(choices=[('STUDENT', 'STUDENT_TYPE'), ('TEACHER', 'TEACHER_TYPE'), ('PARENT', 'PARENT_TYPE')], default='STUDENT', max_length=10)),
                ('address', models.CharField(help_text="user's address", max_length=100)),
                ('roll', models.IntegerField(help_text="student's roll number")),
                ('user', models.OneToOneField(help_text='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
    ]
