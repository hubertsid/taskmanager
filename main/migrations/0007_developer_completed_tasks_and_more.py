# Generated by Django 4.2.6 on 2023-11-02 22:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_developer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='completed_tasks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='developer',
            name='specialization',
            field=models.CharField(choices=[('FRONTEND', 'Frontend'), ('BACKEND', 'Backend'), ('DEVOPS', 'DevOps'), ('UX/UI', 'UX/UI')], default='FRONTEND', max_length=100),
        ),
    ]
