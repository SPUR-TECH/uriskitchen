from django.contrib import admin
from .models import Meal, Dessert, Comment


# @admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


# @admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_Medium', 'price_Large')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'approved')
    list_filter = ('approved',)
    search_fields = ('title', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Meal, MealAdmin)