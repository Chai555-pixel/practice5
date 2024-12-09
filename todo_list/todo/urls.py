# todo/urls.py
from django.urls import path
from .views import home, TaskList  # Import the views for home and TaskList

urlpatterns = [
    path('', home, name='home'),  # Home page route
    path('tasks/', TaskList.as_view(), name='tasks'),  # Task list route
]
