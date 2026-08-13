from django.urls import path

from .views import DepartmentApiView, EmployeeApiView


urlpatterns = [
    path(
        "departments/",
        DepartmentApiView.as_view(),
        name="departments"
    ),

    path(
        "departments/<int:id>/",
        DepartmentApiView.as_view(),
        name="department-detail"
    ),

    path(
        "employees/",
        EmployeeApiView.as_view(),
        name="employees"
    ),

    path(
        "employees/<int:id>/",
        EmployeeApiView.as_view(),
        name="employee-detail"
    ),
]

