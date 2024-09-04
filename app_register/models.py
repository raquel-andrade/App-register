from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True)
    identidade = models.CharField(max_length=20, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

