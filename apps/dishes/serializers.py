from typing import List

from rest_framework import serializers

from apps.dishes.models import Food, FoodCategory, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = (
            'name',
            'description',
            'price',
            'is_special',
            'is_vegan',
            'toppings',
        )

    def get_toppings(self, obj: Food) -> List[str]:
        toppings = obj.toppings.all()
        return [topping.name for topping in toppings]


class CategoryWithFoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = FoodCategory
        fields = (
            'id',
            'name',
            'foods',
        )
