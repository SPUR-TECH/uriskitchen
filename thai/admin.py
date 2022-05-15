from django.contrib import admin
from .models import Meal, Dessert


class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


admin.site.register(Meal, MealAdmin)


class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


admin.site.register(Dessert, DessertAdmin)
