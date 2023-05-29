"""
This file contains different serializer Employee objects.
They handle serialization and deserialization of these objects,
and also include validation and creation/update logic.
The EmployeeGalleryCreateSerializer creates a new employee,
while the EmployeeUpdateSerializer updates an existing employee object.
"""
import re

from rest_framework import serializers

from employee.constants import REGEX, MAX_LENGTH, MIN_LENGTH
from employee.messages import VALIDATION
from employee.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model for listing of Employee objects
    """

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the EmployeeCreateSerializer should work with
        """
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'contact', 'created_at', 'updated_at']


class EmployeeCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model creating a new Employee instance with the required fields:
    The 'error_messages' argument is used to specify custom error messages
    in case of validation errors.
    """
    first_name = serializers.CharField(
        min_length=MIN_LENGTH['first_name'], max_length=MAX_LENGTH['first_name'], required=True, allow_blank=False,
        trim_whitespace=True, error_messages=VALIDATION['first_name']
    )
    last_name = serializers.CharField(
        min_length=MIN_LENGTH['last_name'], max_length=MAX_LENGTH['last_name'], required=True, allow_blank=False,
        trim_whitespace=False, error_messages=VALIDATION['last_name']
    )
    email = serializers.EmailField(
        required=True, allow_blank=False, error_messages=VALIDATION['email']
    )
    contact = serializers.CharField(
        min_length=MIN_LENGTH['contact'], max_length=MAX_LENGTH['contact'], required=True, allow_blank=False,
        error_messages=VALIDATION['contact']
    )

    def validate(self, attrs):
        """
        Custom validation method to check if email already exists.
        """
        email = attrs.get('email')
        if Employee.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': VALIDATION['email']['exists']})
        return attrs

    @staticmethod
    def validate_first_name(value):
        """
        check that the first_name should contain only alphabets
        :param value:first_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["first_name"], value):
            raise serializers.ValidationError(VALIDATION['first_name']['invalid'])
        return value

    @staticmethod
    def validate_last_name(value):
        """
        check that the last_name should contain only alphabets
        :param value:last_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["last_name"], value):
            raise serializers.ValidationError(VALIDATION['last_name']['invalid'])
        return value

    @staticmethod
    def validate_contact(value):
        """
        check that the contact should contain only digits
        :param value:contact
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["contact"], value):
            raise serializers.ValidationError(VALIDATION['contact']['invalid'])
        return value

    def create(self, validated_data):
        """
        Override the create method to add custom behavior
        when creating a new Employee instance
        """
        employee = Employee.objects.create(**validated_data)
        return employee

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the EmployeeCreateSerializer should work with
        """
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'contact', 'created_at']


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model updating an existing Employee instance with the required fields:
    The 'error_messages' argument is used to specify custom error messages
    in case of validation errors.
    """
    first_name = serializers.CharField(
        min_length=MIN_LENGTH['first_name'], max_length=MAX_LENGTH['first_name'], required=True, allow_blank=False,
        trim_whitespace=True, error_messages=VALIDATION['first_name']
    )
    last_name = serializers.CharField(
        min_length=MIN_LENGTH['last_name'], max_length=MAX_LENGTH['last_name'], required=True, allow_blank=False,
        trim_whitespace=False, error_messages=VALIDATION['last_name']
    )
    email = serializers.EmailField(
        required=True, allow_blank=False, error_messages=VALIDATION['email']
    )
    contact = serializers.CharField(
        min_length=MIN_LENGTH['contact'], max_length=MAX_LENGTH['contact'], required=True, allow_blank=False,
        error_messages=VALIDATION['contact']
    )

    @staticmethod
    def validate_first_name(value):
        """
        check that the first_name should contain only alphabets
        :param value:first_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["first_name"], value):
            raise serializers.ValidationError(VALIDATION['first_name']['invalid'])
        return value

    @staticmethod
    def validate_last_name(value):
        """
        check that the last_name should contain only alphabets
        :param value:last_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["last_name"], value):
            raise serializers.ValidationError(VALIDATION['last_name']['invalid'])
        return value

    @staticmethod
    def validate_contact(value):
        """
        check that the contact should contain only digits
        :param value:contact
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["contact"], value):
            raise serializers.ValidationError(VALIDATION['contact']['invalid'])
        return value

    def update(self, instance, validated_data):
        """
        Override the update method to add custom behavior
        when updating an existing Employee instance
        """
        Employee.objects.filter(id=instance.id).update(**validated_data)
        updated_employee = Employee.objects.get(id=instance.id)
        return updated_employee

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the EmployeeUpdateSerializer should work with
        """
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'contact', 'updated_at']
