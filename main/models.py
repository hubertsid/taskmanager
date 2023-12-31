from typing import Any
from django.db import models

# Create your models here.

class Specialization(models.TextChoices):
    FRONTEND = 'FRONTEND', 'Frontend'
    BACKEND = 'BACKEND', 'Backend'
    DEVOPS = 'DEVOPS', 'DevOps'
    UX_UI = 'UX/UI', 'UX/UI'

class Developer(models.Model):
    # Developer's nick
    id = models.CharField(max_length=255, primary_key=True)
    # Developer's name
    name = models.CharField(max_length=255)
    # Developer's specialization
    specialization = models.CharField(
        max_length=100,
        choices=Specialization.choices,
        default=Specialization.FRONTEND
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id

class State(models.TextChoices):
    TO_DO = 'TO_DO', 'To-do'
    IN_PROGRESS = 'IN_PROGRESS', 'In progress'
    COMPLETED = 'COMPLETED', 'Completed'

class Task(models.Model):

    def __init__(self,name=None,project_id=None,
                 credentials=None,state=None,developers=None,estimation=None,
                 created_at=None,created_by=None):
        self.name = name
        self.project_id=project_id,
        self.credentials=credentials,
        self.state=state,
        self.developers=developers,
        self.estimation=estimation,
        self.created_at=created_at,
        self.created_by=created_by


    name = models.CharField(max_length=100, default=None)
    project_id = models.CharField(max_length=100)
    credentials = models.CharField(
        max_length=100,
        choices=Specialization.choices,
        default=Specialization.FRONTEND
    )
    state = models.CharField(
        max_length=100,
        choices=State.choices,
        default=State.TO_DO
    )
    developers = models.ManyToManyField(Developer, default=None)
    estimation = models.IntegerField(default=1)
    created_at = models.DateTimeField()
    created_by = models.CharField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

class Project(models.Model):
    # Project name
    id = models.CharField(max_length=100, primary_key=True)
    # Project creator's name
    user = models.CharField(max_length=100)
    # List of developers in the project
    developers = models.ManyToManyField(Developer, default=None)
    # List of tasks in the project
    tasks = models.ManyToManyField(Task, default=None)