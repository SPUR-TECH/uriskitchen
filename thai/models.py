from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='Meal_Likes')
    comments = models.ManyToManyField(User, related_name='Meal_Comments', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Dessert(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='Dessert_Likes', blank=True)
    comments = models.ManyToManyField(User, related_name='Dessert_Comments', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):  

    title = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    approved = models.BooleanField(default=False)

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)