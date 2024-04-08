from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    role=models.TextField(blank=False , null=True)
    email=models.EmailField(blank=False, null=True)
    def __str__(self):
        return self.role
  

class Product(models.Model):
    name = models.CharField(max_length=100)
    category=models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='items_images',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    is_member = models.BooleanField(default=False)
    membership_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    
    