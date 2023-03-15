from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from tasks.models import Worker, Task


def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks
    }

    return render(request, "tasks/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_list.html"


