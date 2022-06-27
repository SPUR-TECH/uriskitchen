from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    """ This is the models to display the meal menu
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    comments = models.ManyToManyField(
        User, related_name='Meal_Comments', blank=True)

    def __str__(self):
        return self.title


class Dessert(models.Model):
    """ This is the models to display the dessert menu
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    comments = models.ManyToManyField(
        User, related_name='Dessert_Comments', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ This is the models to display the meal comments
    """
    comment = models.TextField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=1)
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal.title


class DessertComment(models.Model):
    """ This is the models to display the dessert comments
    """
    comment = models.TextField()
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, default=1)
    dessert_comment_writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dessert.title
