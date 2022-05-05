from django.shortcuts import render, get_object_or_404, reverse
from .models import Meal, Home, Desert


def home_view(request):
    template = "thai/index.html"
    context = {'active_link': 'index'}
    return render(request, template, context)


def meal_view(request):
    template = "thai/meal.html"
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects, 'active_link': 'meal'}
    return render(request, template, context)


def desert_view(request):
    template = "thai/desert.html"
    desert_objects = Desert.objects.all()
    context = {
        'desert_objects': desert_objects,'active_link': 'desert'}
    return render(request, template, context)


def order_view(request):
    template = "thai/order.html"
    context = {'active_link': 'order'}
    return render(request, template, context)
