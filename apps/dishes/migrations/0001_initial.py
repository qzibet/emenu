# Generated by Django 3.2.5 on 2022-12-19 12:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=60, verbose_name='Название категории')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Публикуется?')),
            ],
            options={
                'verbose_name': 'Категория Блюд',
                'verbose_name_plural': 'Категории Блюд',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=60, verbose_name='Название ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=60, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('is_special', models.BooleanField(default=False, verbose_name='Особенное?')),
                ('is_vegan', models.BooleanField(default=False, verbose_name='Вегетарианское?')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Публикуется?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='dishes.foodcategory', verbose_name='категория')),
                ('toppings', models.ManyToManyField(related_name='foods', to='dishes.Topping', verbose_name='Ингредиенты')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
