from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import User
from .utils import normalise_email

if hasattr(User, 'REQUIRED_FIELDS'):
    if not (User.USERNAME_FIELD == 'email' or 'email' in User.REQUIRED_FIELDS):
        raise ImproperlyConfigured(
            "EmailBackend: Your User model must have an email"
            " field with blank=False")


class EmailBackend(ModelBackend):
    """
    Custom auth backend that uses an email address and password

    For this to work, the User model must have an 'email' field
    """

    def _authenticate(self, request, email=None, password=None, *args, **kwargs):
        if email is None:
            if 'username' not in kwargs or kwargs['username'] is None:
                return None
            clean_email = normalise_email(kwargs['username'])
        else:
            clean_email = normalise_email(email)

        # Check if we're dealing with an email address
        if '@' not in clean_email:
            return None

        matching_users = User.objects.get(email__iexact=clean_email)
        if (matching_users.check_password(password)
                and self.user_can_authenticate(matching_users)):
            # Happy path
            return matching_users
        return None

    def authenticate(self, *args, **kwargs):
        return self._authenticate(*args, **kwargs)
