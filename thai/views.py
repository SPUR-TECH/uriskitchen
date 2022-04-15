from django.shortcuts import render, get_object_or_404, reverse
from .models import Meal, Home, Desert


def home_view(request):
    template = "thai/index.html"
    return render(request, template)


def meal_view(request):
    template = "thai/meal.html"
    return render(request, template)


def desert_view(request):
    template = "thai/desert.html"
    return render(request, template)
