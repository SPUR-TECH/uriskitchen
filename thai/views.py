from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Meal, Dessert
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "thai/index.html")


def meal_view(request):
    request.session.set_expiry(0)
    template = "thai/meal.html"
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects, 'active_link': 'meal'}
    return render(request, template, context)


def dessert_view(request):
    request.session.set_expiry(0)
    template = "thai/dessert.html"
    dessert_objects = Dessert.objects.all()
    context = {
        'dessert_objects': dessert_objects,'active_link': 'dessert'}
    return render(request, template, context)


@csrf_exempt
def cart_view(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['order'] = request.POST.get('orders')
    template = "thai/cart.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def signup_view(request):
    template = "account_signup.html"
    context = {'active_link': 'signup'}
    return render(request, template, context)


def login_view(request):
    template = "account_login.html"
    context = {'active_link': 'login'}
    return render(request, template, context)


def success_view(request):
    order = request.session['order']
    template = "thai/success.html"
    total = request.session.get('total')
    context = {'order': order, 'total': total}
    return render(request, template, context)
