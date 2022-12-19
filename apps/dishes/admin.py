from django.contrib import admin

from apps.dishes.models import Food, FoodCategory, Topping


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass
