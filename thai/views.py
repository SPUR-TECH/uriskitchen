from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Meal, Home, Dessert


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


def dessert_view(request):
    template = "thai/dessert.html"
    dessert_objects = Dessert.objects.all()
    context = {
        'dessert_objects': dessert_objects,'active_link': 'dessert'}
    return render(request, template, context)


def cart_view(request):
    template = "thai/cart.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def signup_view(request):
    template = "signup.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def login_view(request):
    template = "login.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def success_view(request):
    template = "thai/success.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)
