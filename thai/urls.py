from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('meal/', views.meal_view, name='meal_view'),
    path('desert/', views.desert_view, name='desert_view')
]
