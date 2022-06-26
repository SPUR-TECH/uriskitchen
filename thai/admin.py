from django.contrib import admin
from .models import Meal, Dessert, Comment, DessertComment


# @admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


# @admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


class DessertCommentsAdmin(admin.ModelAdmin):
    list_display = ('dessert', 'comment', 'dessert_comment_writer')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('meal', 'comment', 'comment_writer')


admin.site.register(Comment, CommentsAdmin)
admin.site.register(DessertComment, DessertCommentsAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Meal, MealAdmin)
