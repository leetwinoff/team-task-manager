from django.urls import path

from tasks.views import index, TaskListView, TaskDetailView

urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]

app_name = "tasks"
