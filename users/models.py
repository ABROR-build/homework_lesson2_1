from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9)
