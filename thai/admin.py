from django.contrib import admin
from .models import Meal, Desert


class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


admin.site.register(Meal, MealAdmin)


class DesertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


admin.site.register(Desert, DesertAdmin)
