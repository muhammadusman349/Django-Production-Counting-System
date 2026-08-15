from rest_framework import generics, permissions

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentApiView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)


class EmployeeApiView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)