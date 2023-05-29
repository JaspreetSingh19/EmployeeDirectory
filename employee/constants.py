"""
This file contains various constants used throughout the module.
"""
REGEX = {
    "first_name": r'^[a-zA-Z]+$',
    "last_name": r'^[a-zA-Z]+$',
    "contact": r'^\d+$',
}

MAX_LENGTH = {
    'first_name': 30,
    'last_name': 30,
    'contact': 10,
}

MIN_LENGTH = {
    'first_name': 3,
    'last_name': 3,
    'contact': 10,
}

CREATE = 'create'
UPDATE = 'update'
