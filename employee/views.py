"""
This file contains different ViewSet for 'Employee'
The EmployeeViewSet handles CRUD operations for the Employee model.
"""
from rest_framework import viewsets, status
from rest_framework.response import Response

from employee.constants import CREATE, UPDATE
from employee.messages import SUCCESS_MESSAGES
from employee.models import Employee
from employee.serializers import EmployeeListSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    The EmployeeViewSet handles CRUD operations for the Employee model,
    It provides a serializer class for each action and
    filters queryset based on the id.
    """
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = Employee

    def get_serializer_class(self):
        """
        The get_serializer_class returns a serializer class based on the action being performed.
        For 'create' action, it returns EmployeeCreateSerializer,
        for 'update' action, it returns EmployeeUpdateSerializer,
        and for all other actions, it returns the default serializer, EmployeeListSerializer.
        :return: serializer class
        """
        if self.action == CREATE:
            return EmployeeCreateSerializer
        if self.action == UPDATE:
            return EmployeeUpdateSerializer
        return EmployeeListSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Employee Model objects
        It orders the queryset based on the ID of the objects.
        :return: Employee objects
        """
        queryset = self.queryset.objects.all().order_by('-id')
        return queryset

    def list(self, request, *args, **kwargs):
        """
        The list retrieves all instances of the Employee model.
        serializes them using the serializer returned by the get_serializer() method,
        and returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Employee instances
        """
        if not self.get_queryset().exists():
            return Response({"message": SUCCESS_MESSAGES['employee']['no_employees']}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        This method retrieves a single instance of the Employee model
        using the provided primary key (pk).
        It then serializes the instance using the serializer defined for the view and
        returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Single Image Gallery instance
        """
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        This method creates a new instance of the Employee model using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: employee object
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['employee']['created_successfully'], 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        This method updates an existing instance of the Employee model, based on the primary key (pk)
        using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: updated employee object
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['employee']['updated_successfully'], 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        This method updates an existing instance of the Employee model, based on the primary key (pk)
        using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: updated employee object
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['employee']['updated_successfully'], 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        This method deletes an instance of the Employee model using the primary key
        It returns a success response with a message after the deletion is complete.
        :return: success response
        """
        instance = self.get_object()
        instance.delete()
        return Response({'message': SUCCESS_MESSAGES['employee']['deleted_successfully']}, status=status.HTTP_200_OK)
