from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        messages.success(self.request, "Task created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating task. Please check the form.")
        return super().form_invalid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating task. Please check the form.")
        return super().form_invalid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task deleted successfully!")
        return super().delete(request, *args, **kwargs)


def task_toggle_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()

    status = "completed" if task.is_completed else "marked as pending"
    messages.success(request, f'Task "{task.title}" has been {status}!')

    return redirect("task_detail", pk=task.pk)
