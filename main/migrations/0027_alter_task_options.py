# Generated by Django 4.2.6 on 2023-11-05 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_task_developers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['id']},
        ),
    ]
