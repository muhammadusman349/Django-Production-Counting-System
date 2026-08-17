from rest_framework import generics, permissions
from .models import ProductionBatch
from .serializers import ProductionBatchSerializer
from accounts.permissions import IsAdminOrReadOnly


class ProductionBatchApiView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductionBatchSerializer
    queryset = ProductionBatch.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)