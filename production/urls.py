from django.urls import path

from .views import ProductionBatchApiView


urlpatterns = [
    path("batches/",ProductionBatchApiView.as_view(),name="production-batch-list-create"),
    path("batches/<int:id>/",ProductionBatchApiView.as_view(),name="production-batch-detail"),
    path("worker-assignments/",WorkerAssignmentApiView.as_view(),name="worker-assignment-list-create"),
    path("worker-assignments/<int:id>/",WorkerAssignmentApiView.as_view(),name="worker-assignment-detail"),
]