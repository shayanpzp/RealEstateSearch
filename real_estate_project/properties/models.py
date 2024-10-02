from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50, choices=[('apartment', 'Apartment'), ('house', 'House')])
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=6, decimal_places=2)  # In square meters
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)

    def __str__(self):
        return self.title
