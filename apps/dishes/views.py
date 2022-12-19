from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.dishes.filters import CategoryWithFoodFilter
from apps.dishes.models import FoodCategory
from apps.dishes.serializers import CategoryWithFoodListSerializer


class CategoryWithFoodListView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(
        is_publish=True, foods__is_publish=True
    )
    serializer_class = CategoryWithFoodListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryWithFoodFilter

