from django.db import models

# Create your models here.
class EmployeeRole(models.TextChoices):
    INCHARGE = "INCHARGE", "Incharge"
    STITCHER_WORKER = "STITCHER_WORKER", "Stitcher Worker"
    FINAL_KNOT_WORKER = "FINAL_KNOT_WORKER", "Final Knot Worker"
    QC = "QC", "QC"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    role = models.CharField(max_length=50, choices=EmployeeRole.choices)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    