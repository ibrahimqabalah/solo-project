from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['fname'])<4:
            errors['fname']="First name should be a t least 4 characters!"
        if len(postData['lname'])<4:
            errors['lname']="Last name should be a t least 4 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email']="Invalid Email Address"
        if len(postData['password'])<8:
            errors['password']="Password should be a t least 8 characters!"
        if postData['password'] != postData['confirm']:
            errors['confirm']="Passwords don't match!"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)    
    email = models.EmailField(max_length=45)
    admin = models.BooleanField(blank=False, null =False)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=UserManager()

class Product(models.Model):
    image_url = models.TextField(blank=False, null=False)
    title = models.CharField(max_length=45)
    price = models.IntegerField(default=0)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=45) 
    product_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.product_price * self.quantity

class Purchase(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=45) 
    product_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    @property
    def get_total_price(self):
        return self.product_price * self.quantity
    