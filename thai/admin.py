from django.contrib import admin
from .models import Meal, Dessert, Comment


# @admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


# @admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


admin.site.register(Comment)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Meal, MealAdmin)