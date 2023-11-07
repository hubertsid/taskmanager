from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("main.urls")),
    path('project/', include("main.urls")),
    path('users/', include("main.urls")),
    path('tasks/', include("main.urls")),
    path('admin/', admin.site.urls),
]
