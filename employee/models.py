from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100);
    last_name = models.CharField(max_length=100);
    photo = models.ImageField(upload_to='images')
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True) # block true matlab zaror fill karna
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # show first name to table 
    # string representation
    def __str__(self):
        return self.first_name
