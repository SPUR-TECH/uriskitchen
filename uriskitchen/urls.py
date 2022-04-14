from django.contrib import admin
from django.urls import path
from thai.views import meal_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', meal_view),
]
