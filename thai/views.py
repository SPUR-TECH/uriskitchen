from django.shortcuts import render
from .models import Meal, Home, Desert


def home_view(request):
    home_objects = Home.objects.all()
    context = {
        'home_objects': home_objects
    }
    return render(request, "index.html", context)


def meal_view(request):
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects
    }
    return render(request, "meal.html", context)


def desert_view(request):
    desert_objects = Desert.objects.all()
    context = {
        'desert_objects': desert_objects
    }
    return render(request, "desert.html", context)
