from django.contrib import admin
from django.urls import path
from thai.views import meal_view, home_view, desert_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('meal/', meal_view),
    path('desert/', desert_view),
]
