# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .form import TaskForm


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'tasks': tasks})


def edit_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def complete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')


def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


def delete_task(request, pk):  # Change 'task_id' to 'pk'
    task = get_object_or_404(TaskModel, pk=pk)
    task.delete()
    return redirect('completed_tasks')
