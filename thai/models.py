from django.db import models
from cloudinary.models import CloudinaryField


class Home(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Meal(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Dessert(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Success(models.Model):
    title = models.CharField(max_length=120)
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
    