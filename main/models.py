from django.db import models

# Create your models here.

class Specialization(models.TextChoices):
    FRONTEND = 'FRONTEND', 'Frontend'
    BACKEND = 'BACKEND', 'Backend'
    DEVOPS = 'DEVOPS', 'DevOps'
    UX_UI = 'UX/UI', 'UX/UI'

class Developer(models.Model):
    #developers nick
    id = models.CharField(max_length=255,primary_key=True)
    #developers name
    name = models.CharField(max_length=255)
    #developers specialization
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
    name = models.CharField(max_length=100,default="Unnamed")
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

    class Meta():
        ordering = ["id"]

    def __str__(self):
        return str(self.id)
    

class Project(models.Model):
    # nazwa projektu
    id = models.CharField(max_length=100, primary_key=True)
    # nazwa twórcy projektu
    user = models.CharField(max_length=100)
    # lista deweloperów w projekcie
    developers = models.ManyToManyField(Developer, default=None)
    # lista tasków w projekcie
    tasks = models.ManyToManyField(Task, default=None)