from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {
            "fields": ("years_of_experience", "phone_number"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("years_of_experience", "phone_number")}),
    )