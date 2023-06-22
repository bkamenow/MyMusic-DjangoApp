import re
from django.core.exceptions import ValidationError


def validate_positive_number(value):
    if value < 0:
        raise ValidationError(
            f'{value} must be a positive number! ',
            params={'value': value},
        )


def validate_value_contains_only_letters_numbers_underscores(value):
    pattern = r'\w+$'
    match = re.match(pattern, value)
    if not match:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
