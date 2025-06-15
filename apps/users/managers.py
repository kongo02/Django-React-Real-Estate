from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def validate_required_field(self, field, field_name):
        if not field:
            raise ValueError(_(f"{field_name} required."))

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Valid email address required."))

    def create_user(self, username, first_name, last_name, email, password=None, **extra_fields):
        """
        Creates and returns a user with username, first name, last name, email, and password.
        """
        self.validate_required_field(username, "Username")
        self.validate_required_field(first_name, "First name")
        self.validate_required_field(last_name, "Last name")
        self.validate_required_field(email, "Email address")
        self.validate_required_field(password, "Password")

        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with username, first name, last name, email, and password.
        """
        # Forcefully set required superuser flags
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True

        self.validate_required_field(password, "Password")
        self.validate_required_field(email, "Email address")

        email = self.normalize_email(email)
        self.email_validator(email)

        return self.create_user(username, first_name, last_name, email, password, **extra_fields)
