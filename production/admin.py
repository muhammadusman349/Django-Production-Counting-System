from django.contrib import admin

from .models import ProductionBatch


@admin.register(ProductionBatch)
class ProductionBatchAdmin(admin.ModelAdmin):

    list_display = [
        "batch_number",
        "article",
        "article_size",
        "target_quantity",
        "status",
        "created_by",
        "created_at",
    ]

    list_filter = [
        "status",
        "article",
        "created_at",
    ]

    search_fields = [
        "batch_number",
        "article__name",
        "article__article_code",
        "created_by__email",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]

    ordering = [
        "-created_at"
    ]