from django.db import models
from django.core.validators import validate_email

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {} 
        if len(post_data["first_name"]) < 1:
            errors["first_name"] = "Please enter your first name"
        if len(post_data["last_name"]) < 1:
            errors["last_name"] = "Please enter your last name"
        try: 
            validate_email(post_data["email"])
        except:
            errors["email"] = "Please enter a valid email"
        if len(post_data["password"]) < 1:
            errors["password"] = "Please enter a password"
        if post_data["password"] != post_data["pw_conf"]:
            errors["confirmation"] = "Your password didn't match!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager() # Overriding objects

class Hat(models.Model):
    brand = models.CharField(max_length=60)
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="hats")