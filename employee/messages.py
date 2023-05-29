"""
This file defines dictionaries containing validation error messages and success messages
for the 'employee' app.
The VALIDATION dictionary contains error messages for form validation,
while the SUCCESS_MESSAGES dictionary contains success messages for various operations in the app.
"""
VALIDATION = {
    'first_name': {
        "blank": "first name can not be blank",
        "invalid": "first name must contain only alphabets",
        "required": "first name required",
    },
    'last_name': {
        "blank": "last name can not be blank",
        "invalid": "last name must contains only alphabets",
        "required": "last name required",
    },
    'email': {
        "blank": "Email can not be blank",
        "required": "Email required",
        "exists": "email already exist",
    },
    'contact': {
        "blank": "contact can not be blank",
        "required": "contact required",
        "invalid": "invalid contact"
    },
}

SUCCESS_MESSAGES = {
    "employee": {
        "created_successfully": "Employee created successfully",
        "updated_successfully": "Employee updated successfully",
        "deleted_successfully": "Employee deleted successfully",
        "no_employees": "No employees found"
    },

}
