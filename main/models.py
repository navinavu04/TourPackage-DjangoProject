from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='package_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.package.title}"
