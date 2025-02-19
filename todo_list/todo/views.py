# todo/views.py
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

# Home view
def home(request):
    return render(request, 'todo/home.html')  # Render the home template

# Task list view (class-based view)
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # The context variable for the task list
    template_name = 'todo/task_list.html'  # Template name (optional, defaults to 'todo_list/task_list.html')
