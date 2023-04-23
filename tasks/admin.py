from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Task, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("years_of_experience",),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "deadline_date",
        "is_completed",
        "priority",
        "task_type",
    )
    search_fields = ("name",)
    list_filter = ("deadline_date", "priority")


admin.site.register(TaskType)
admin.site.register(Position)
