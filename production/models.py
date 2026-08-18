from django.db import models
from accounts.models import User
from articles.models import Article, ArticleSize
from employees.models import Employee

# Create your models here.
class ProductionPhase(models.TextChoices):
    MATCHING = "MATCHING", "Matching"
    SORTING_1 = "SORTING_1", "1st Sorting"
    SORTING_2 = "SORTING_2", "2nd Sorting"
    STITCHING = "STITCHING", "Stitching"
    FINAL_KNOT = "FINAL_KNOT", "Final Knot"
    QC = "QC", "QC"


class ProductionBatchStatus(models.TextChoices):
    PLANNED = "PLANNED", "Planned"
    MATCHING = "MATCHING", "Matching"
    STITCHING = "STITCHING", "Stitching"
    FINAL_KNOT = "FINAL_KNOT", "Final Knot"
    QC = "QC", "QC"
    COMPLETED = "COMPLETED", "Completed"
    CLOSED = "CLOSED", "Closed"
    CANCELLED = "CANCELLED", "Cancelled"


class ProductionBatch(models.Model):
    batch_number = models.CharField(max_length=100,unique=True)
    article = models.ForeignKey(Article,on_delete=models.PROTECT,related_name="production_batches")
    article_size = models.ForeignKey(ArticleSize,on_delete=models.PROTECT,related_name="production_batches")
    target_quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20,choices=ProductionBatchStatus.choices,default=ProductionBatchStatus.PLANNED)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name="created_production_batches")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.batch_number


class WorkerAssignment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT,related_name="worker_assignments")
    production_batch = models.ForeignKey(ProductionBatch,on_delete=models.PROTECT,related_name="worker_assignments")
    production_phase = models.CharField(max_length=20,choices=ProductionPhase.choices)
    assigned_date = models.DateField()
    target_quantity = models.PositiveIntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name="created_worker_assignments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name="updated_worker_assignments")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.name} - {self.production_batch.batch_number}"