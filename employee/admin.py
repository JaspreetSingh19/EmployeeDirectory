"""
This file defines Django admin `EmployeeAdmin` representing Employee.
These are associated with their respective models Employee in the meta class.
"""
from django.contrib import admin

from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact', 'created_at', 'updated_at')

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
