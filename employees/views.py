from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            department = self.get_object()
            serializer = self.get_serializer(department)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        departments = self.get_queryset()
        serializer = self.get_serializer(
            departments,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def get_object(self):
        return generics.get_object_or_404(
            self.get_queryset(),
            id=self.kwargs["id"]
        )


class EmployeeApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            employee = self.get_object()
            serializer = self.get_serializer(employee)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        employees = self.get_queryset()
        serializer = self.get_serializer(
            employees,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def get_object(self):
        return generics.get_object_or_404(
            self.get_queryset(),
            id=self.kwargs["id"]
        )

