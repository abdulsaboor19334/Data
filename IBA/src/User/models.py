from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager



class BaseManager(BaseUserManager):
    def create_user(self, email,first_name, last_name, erp,password=None):
        if not email:
            raise ValueError('Email Field is Required')
        if not first_name:
            raise ValueError('First Name is Required')
        if not last_name:
            raise ValueError('Last name  is Required')
        if not erp:
            raise ValueError('Erp is required is Required')
        if not password:
            raise ValueError('Password is required is Required')
        

        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            erp = erp
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    def create_superuser(self, email,first_name, last_name, erp,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            erp = erp,
            password = password,
        )
        user.staff = True 
        user.admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,first_name, last_name, erp,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            erp = erp,
            password = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50,unique=True)
    last_name =models.CharField(max_length=50,unique=True)
    erp = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'erp',
    ]

    options = BaseManager()

    def get_username(self):
        return self.email
    
    def get_erp(self):
        return self.erp
    
    def get_fullname(self):
        return self.first_name +' '+ self.last_name +' '+ self.erp
    
    @property
    def is_admin(self):
        return self.is_admin
    @property
    def is_staff(self):
        return self.is_staff
    @property
    def is_active(self):
        return self.is_active

