from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Meal, Home, Desert
from django.contrib.auth.forms import UserCreationForm


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


def cart_view(request):
    template = "thai/cart.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def signup_view(request):
    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, 'thai/signup.html', context)
