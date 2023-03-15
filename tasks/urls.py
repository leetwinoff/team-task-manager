from django.urls import path

from tasks.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view, name="task-delete")
]

app_name = "tasks"
