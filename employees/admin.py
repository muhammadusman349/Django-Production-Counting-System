from django.contrib import admin

from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "employee_code",
        "name",
        "email",
        "role",
        "department",
        "is_active",
        "created_at",
    )

    list_filter = (
        "role",
        "department",
        "is_active",
    )

    search_fields = (
        "employee_code",
        "name",
        "email",
    )

    ordering = (
        "-created_at",
    )
