from uuid import uuid4
from factory.django import DjangoModelFactory
from factory import faker, fuzzy, SubFactory, post_generation

from apps.dishes.models import Food, FoodCategory, Topping


class ToppingFactory(DjangoModelFactory):
    name = faker.Faker("text", max_nb_chars=60)

    class Meta:
        model = Topping


class FoodCategoryFactory(DjangoModelFactory):
    name = faker.Faker("text", max_nb_chars=60)
    is_publish = faker.Faker('boolean')

    class Meta:
        model = FoodCategory


class FoodFactory(DjangoModelFactory):
    name = faker.Faker("text", max_nb_chars=60)
    description = faker.Faker('text')
    price = fuzzy.FuzzyDecimal(100, 4000)
    is_special = faker.Faker('boolean')
    is_vegan = faker.Faker('boolean')
    is_publish = faker.Faker('boolean')
    category = SubFactory(FoodCategoryFactory)
    toppings = SubFactory(ToppingFactory)

    @post_generation
    def toppings(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for topping in extracted:
                self.toppings.add(topping)

    class Meta:
        model = Food
