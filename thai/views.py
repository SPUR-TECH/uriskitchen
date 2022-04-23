from django.shortcuts import render, get_object_or_404, reverse
from .models import Meal, Home, Desert


def home_view(request):
    template = "thai/index.html"
    return render(request, template)


def meal_view(request):
    template = "thai/meal.html"
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects}
    return render(request, template, context)


def desert_view(request):
    template = "thai/desert.html"
    desert_objects = Desert.objects.all()
    context = {
        'desert_objects': desert_objects}
    return render(request, template, context)
