from django.shortcuts import render
from .models import Meal


def meal_view(request):
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects
    }
    return render(request, "meal.html", context)
