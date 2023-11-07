from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),#index
    path("project/", views.project, name="project"),#add project and display all projects
    path("project/<str:id>", views.project_info, name="project_info"),# display developers and tasks
    path("project/<str:id>/tasks", views.tasks, name="tasks"),# tasks in the project
    path("project/<str:id>/assignment", views.assignment, name="assignment"),
    path("project/<str:id>/assignment/<str:assignment_id>", views.assignment_add_dev, name="assignment_add_dev"),
    path('project/<str:id>/task/<int:task_id>', views.edit_task_status, name='edit_task_status'),
    path("tasks/", views.tasks, name="tasks"),
    path("users/", views.users, name="users"),
]