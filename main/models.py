from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from datetime import date 

class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='package_images/')
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, null=True)
    is_approved = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.package.title} on {self.date}"

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.company_name

