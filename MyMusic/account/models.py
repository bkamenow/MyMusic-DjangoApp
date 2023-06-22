from django.core.validators import MinLengthValidator
from django.db import models

from custom_validators.validators import validate_positive_number, \
    validate_value_contains_only_letters_numbers_underscores


# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=15,
                                validators=[
                                    MinLengthValidator(2),
                                    validate_value_contains_only_letters_numbers_underscores,
                                ])
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(validators=[validate_positive_number])
