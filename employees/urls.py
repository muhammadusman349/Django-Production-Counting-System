from django.urls import path

from .views import (
    DepartmentApiView,
    EmployeeApiView,
)


urlpatterns = [
    # Department
    path("departments/",DepartmentApiView.as_view(),name="department-list-create"),
    path("departments/<int:id>/",DepartmentApiView.as_view(),name="department-detail"),

    # Employee
    path("employees/",EmployeeApiView.as_view(),name="employee-list-create"),
    path("employees/<int:id>/",EmployeeApiView.as_view(),name="employee-detail"),
]