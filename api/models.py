from django.db import models
from django.core import validators

class User(models.Model):
    name = models.CharField(max_length=100, validators=[validators.validate_unicode_slug])
