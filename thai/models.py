from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    comments = models.ManyToManyField(User, related_name='Meal_Comments', blank=True)

    def __str__(self):
        return self.title


class Dessert(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    comments = models.ManyToManyField(User, related_name='Dessert_Comments', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=1)
    comment_writer = models.ManyToManyField(User)

    def __str__(self):
        return self.meal.title


class DessertComment(models.Model):
    body = models.TextField()
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.dessert.title
