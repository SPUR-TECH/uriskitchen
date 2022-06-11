from django.db import models
from django.contrib.auth.models import User
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
    likes = models.ManyToManyField(User, related_name='Meal_Likes')

    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


class Dessert(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_Medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_Large = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='Dessert_Likes', blank=True)

    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):  
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"Comment {self.body} by {self.name}"
