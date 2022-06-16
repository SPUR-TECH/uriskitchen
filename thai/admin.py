from django.contrib import admin
from .models import Meal, Dessert, Comment, DessertComment


# @admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


# @admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


class DessertComments(admin.ModelAdmin):
    list_display = ('dessert.title', 'body')


class Comments(admin.ModelAdmin):
    list_display = ('meal.title', 'body')


admin.site.register(Comment)
admin.site.register(DessertComment)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Meal, MealAdmin)
