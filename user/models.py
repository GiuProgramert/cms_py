# accounts/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    roles = models.ManyToManyField('Role', related_name='users', blank=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Specify a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Specify a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, related_name='roles', blank=True)

    def __str__(self):
        return self.name