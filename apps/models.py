from itertools import product
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Product(models.Model):
    """
    This Model is used to store Product data in Database
    """
    per = 'per'
    value ='value'
    discount_type_choice= (
      (per,'Percentage'),
      (value,'Value'),      
    )
    name = models.CharField(max_length=200)
    price=  models.IntegerField(null=True,blank=True)   
    discount_type=models.CharField(max_length=15, choices=discount_type_choice, default=per)
    discount_value=models.IntegerField(null=True,blank=True,default=10)
   
    # published_date = models.DateTimeField(blank=True, null=True)   

    def __str__(self):
        return self.name
    
class Order(models.Model):
    """
    This Model is used to store Order data in Database
    """
   
    user_email = models.CharField(max_length=200)
    product=  models.ManyToManyField(Product)  
    created_date = models.DateTimeField()
    price=models.IntegerField()
      

    def __str__(self):
        return self.user_email


class OrderProduct(models.Model):
    """
    This Model is used to store Order data in Database
    """
   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price= models.IntegerField()      

    def __str__(self):
        return self.id
      
  
class User(AbstractUser):
    """
    This Model is used to store  data in Database
    """
    admin = 'admin'
    user ='user'
    role_choice= (
      (admin,'Admin'),
      (user,'User'),      
    )
    username = models.CharField(
        max_length=150,
        unique=True,
       null=True,
       blank=True
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=15, choices=role_choice, default=user)   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.email

