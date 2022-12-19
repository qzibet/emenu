from random import choice

from django.urls import reverse

from rest_framework.test import APITestCase

from apps.dishes.models import FoodCategory
from apps.dishes.tests.factories import (
    FoodFactory, FoodCategoryFactory
)


class DishesTest(APITestCase):
    def setUp(self) -> None:
        self.categories = FoodCategoryFactory.create_batch(5)
        self.published_categories = len(
            [category.is_publish for category in self.categories]
        )
        category_ids = [category.id for category in self.categories]
        self.foods = FoodFactory.create_batch(
            5, category_id=choice(category_ids)
        )
        self.url = reverse('food-list')
        self.categories_query = FoodCategory.objects.filter(
            is_publish=True, foods__is_publish=True
        )

    def test_category_publish(self) -> None:
        category_count = self.categories_query.count()
        response = self.client.get(self.url).data
        response_category_count = response.get('count')
        self.assertEqual(response_category_count, category_count)

    def test_is_vegan_filter(self) -> None:
        is_vegan_foods = self.categories_query.filter(
            foods__is_vegan=True
        ).distinct().count()
        response = self.client.get(self.url, {'is_vegan': 'true'}).data

        categories = response.get('results')
        foods = []
        for category in categories:
            if category.get('foods'):
                foods.append(category.get('foods'))

        self.assertEqual(len(foods), is_vegan_foods)

    def test_is_special_filter(self) -> None:
        is_special_foods = self.categories_query.filter(
            foods__is_special=True
        ).distinct().count()
        response = self.client.get(self.url, {'is_special': 'true'}).data

        categories = response.get('results')
        foods = []
        for category in categories:
            if category.get('foods'):
                foods.append(category.get('foods'))

        self.assertEqual(len(foods), is_special_foods)

    def test_is_special_and_is_vegan_filter(self) -> None:
        is_special_and_is_vegan_foods = self.categories_query.filter(
            foods__is_special=True, foods__is_vegan=True
        ).distinct().count()
        response = self.client.get(
            self.url, {'is_vegan': 'true', 'is_special': 'true'}
        ).data

        categories = response.get('results')
        foods = []
        for category in categories:
            if category.get('foods'):
                foods.append(category.get('foods'))

        self.assertEqual(len(foods), is_special_and_is_vegan_foods)

    def tearDown(self) -> None:
        FoodCategory.objects.all().delete()
