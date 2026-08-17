from rest_framework import serializers

from .models import ProductionBatch


class ProductionBatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionBatch

        fields = [
            "id",
            "batch_number",
            "article",
            "article_size",
            "target_quantity",
            "status",
            "created_by",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]
