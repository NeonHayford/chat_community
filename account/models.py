from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.settings import AUTH_USER_MODEL
from uuid import uuid4
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address')
        if not password:
            raise ValueError('You must provide a password')
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        try:
            user = self.create_user(
                email = email,
                password = password,
                **extra_fields
                )
            return user
        except:
            raise ValueError('Uh-Oh! We Encountered an Issue. Please Retry.')
        


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='profile/')
    bio = models.TextField(default='Descripe yourself...')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)