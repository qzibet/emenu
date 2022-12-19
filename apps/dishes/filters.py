from django.db.models import Prefetch
from django_filters import rest_framework as filters

from apps.dishes.models import FoodCategory, Food


class CategoryWithFoodFilter(filters.FilterSet):
    is_vegan = filters.BooleanFilter(method='is_vegan_filter')
    is_special = filters.BooleanFilter(method='is_special_filter')
    toppings = filters.CharFilter(method='toppings_filter')

    class Meta:
        model = FoodCategory
        fields = (
            'is_vegan',
            'is_special',
            'toppings',
        )

    def is_vegan_filter(self, query, _, value):
        return query.prefetch_related(
            'foods'
        ).filter(foods__is_vegan=value).distinct()

    def is_special_filter(self, query, _, value):
        return query.prefetch_related(
            'foods'
        ).filter(foods__is_special=value).distinct()

    def toppings_filter(self, query, _, value):
        value = value.split('|') if '|' in value else [value]
        return query.prefetch_related(
            Prefetch(
                'foods',
                queryset=Food.objects.prefetch_related(
                    'toppings'
                ).filter(toppings__name__=value).distinct(),
            )).distinct()
