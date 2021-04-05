from django.contrib.auth.models import AbstractUser
from django.db import models


class UkUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="age")