from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='название ингидиента')
    ingredient_amount = models.FloatField(verbose_name='грамм')

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингридиенты'

    def __str__(self):
        return f'{self.name}'


class Meal(models.Model):

    name = models.CharField(max_length=20, unique=True, verbose_name='название блюда')
    price = models.FloatField(verbose_name='цена блюда')
    ingredient = models.ManyToManyField(Ingredient, verbose_name='ингредиенты', related_name='meals')

    class Meta:

        db_table = 'meal'
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return f'{self.name}'

