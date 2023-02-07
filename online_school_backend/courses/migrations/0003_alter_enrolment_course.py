# Generated by Django 4.1.5 on 2023-02-07 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_enrolment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolment',
            name='course',
            field=models.OneToOneField(help_text='available courses', on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
