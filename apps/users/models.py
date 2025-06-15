import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from apps.users.managers import CustomUserManager
from django.db import models


class User(AbstractUser, PermissionsMixin):
    """
    Custom user model that extends AbstractUser and PermissionsMixin.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("UserName"),
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last Name"),
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email Address"),
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Date Joined"),
    )
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["username","first_name","last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        """
        Returns the full name of the user.
        """
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def get_short_name(self):
        return self.username.title()