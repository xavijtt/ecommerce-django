from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


    
    
class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, True, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)
        
class Account(AbstractBaseUser,PermissionsMixin):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    username =models.CharField(max_length=50, unique=True)
    email =models.CharField(max_length=100,unique=True)
    phone_number =models.CharField(max_length=50)
    
    #campos atributos de django
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    objects=UserManager()
    
    def get_short_name(self):
        return self.email
    
    
    
    
    
