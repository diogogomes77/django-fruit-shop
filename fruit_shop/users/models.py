from django.contrib.auth.models import User, UserManager
from django.db import models


class BaseUser(User):
    """User with app settings."""
    timezone = models.CharField(max_length=50, default='Europe/Paris')

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()


class Admin(BaseUser):
    pass


class Customer(BaseUser):
    pass