from django.db import models
from accounts.models import User
from articles.models import Article, ArticleSize

# Create your models here.

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