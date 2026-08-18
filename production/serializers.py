from rest_framework import serializers
from .models import ProductionBatch, WorkerAssignment


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

    def validate(self, attrs):

        article = attrs.get("article")
        article_size = attrs.get("article_size")

        if article and article_size:

            if article_size.article_id != article.id:
                raise serializers.ValidationError({
                    "article_size": (
                        "This article size does not belong "
                        "to the selected article."
                    )
                })

        return attrs


class WorkerAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkerAssignment

        fields = [
            "id",
            "employee",
            "production_batch",
            "production_phase",
            "assigned_date",
            "target_quantity",
            "is_active",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        ]

    def validate(self, attrs):

        employee = attrs.get("employee")

        # For create, is_active defaults to True
        is_active = attrs.get("is_active", True)

        if employee and is_active:

            active_assignment = WorkerAssignment.objects.filter(
                employee=employee,
                is_active=True
            )

            # Don't compare the object with itself during update
            if self.instance:
                active_assignment = active_assignment.exclude(
                    id=self.instance.id
                )

            if active_assignment.exists():
                raise serializers.ValidationError({
                    "employee": (
                        "This employee already has an active "
                        "worker assignment."
                    )
                })

        return attrs