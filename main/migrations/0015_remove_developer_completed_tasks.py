# Generated by Django 4.2.6 on 2023-11-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_developer_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='completed_tasks',
        ),
    ]
