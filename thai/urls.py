from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('meal/', views.meal_view, name='meal_view'),
    path('desert/', views.desert_view, name='desert_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
