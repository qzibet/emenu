from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel


class Food(AbstractModel):
    name = models.CharField(max_length=60, verbose_name=_('Название блюда'))
    description = models.TextField(verbose_name=_('Описание'))
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена'),
    )
    is_special = models.BooleanField(
        default=False, verbose_name=_('Особенное?')
    )
    is_vegan = models.BooleanField(
        default=False, verbose_name=_('Вегетарианское?')
    )
    is_publish = models.BooleanField(
        default=False, verbose_name=_('Публикуется?')
    )
    category = models.ForeignKey(
        'dishes.FoodCategory',
        on_delete=models.CASCADE,
        related_name='foods',
        verbose_name=_('категория'),
    )
    toppings = models.ManyToManyField(
        'dishes.Topping',
        related_name='foods',
        verbose_name=_('Ингредиенты')
    )

    class Meta:
        verbose_name = _('Блюдо')
        verbose_name_plural = _('Блюда')

    def __str__(self) -> str:
        return self.name


class FoodCategory(AbstractModel):
    name = models.CharField(
        max_length=60, verbose_name=_('Название категории')
    )
    is_publish = models.BooleanField(
        default=False, verbose_name=_('Публикуется?')
    )

    class Meta:
        verbose_name = _('Категория Блюд')
        verbose_name_plural = _('Категории Блюд')

    def __str__(self) -> str:
        return self.name


class Topping(AbstractModel):
    name = models.CharField(
        max_length=60, verbose_name=_('Название ингредиента')
    )

    class Meta:
        verbose_name = _('Ингредиент')
        verbose_name_plural = _('Ингредиенты')

    def __str__(self) -> str:
        return self.name
