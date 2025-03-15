from django.db import models

from django.contrib.auth.models import AbstractUser

class UserProfil(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username =models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.username