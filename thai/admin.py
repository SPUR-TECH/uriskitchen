from django.contrib import admin
from .models import Meal, Dessert, Comment, DessertComment


class MealAdmin(admin.ModelAdmin):
    """Meal menu in admin area
    """
    list_display = ('title', 'price_Medium', 'price_Large')


class DessertAdmin(admin.ModelAdmin):
    """Dessert menu in admin area
    """
    list_display = ('title', 'price_Medium', 'price_Large')


class DessertCommentsAdmin(admin.ModelAdmin):
    """Dessert comments in admin area
    """
    list_display = ('dessert', 'comment', 'dessert_comment_writer')


class CommentsAdmin(admin.ModelAdmin):
    """Meal comments in admin area
    """
    list_display = ('meal', 'comment', 'comment_writer')


admin.site.register(Comment, CommentsAdmin)
admin.site.register(DessertComment, DessertCommentsAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Meal, MealAdmin)
