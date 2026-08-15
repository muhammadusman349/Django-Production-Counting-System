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

    def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)


class EmployeeApiView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)
