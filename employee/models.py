"""
This module defines Django model `Employee` representing employee .
This model is associated with its respective database table specified in its `Meta` class.
"""
from django.db import models


class Employee(models.Model):
    """
    Custom employee model that extends the built-in Django model
    with additional fields for Employee model

    * email is unique
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=True, blank=True)
    contact = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.first_name)

    class Meta:
        """
        Use the Meta class to specify the database table
        for Employee model
        """
        db_table = 'Employee'
