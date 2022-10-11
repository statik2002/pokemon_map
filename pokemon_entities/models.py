from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    image = models.ImageField('Изображение покемона', upload_to='pokemons_images/', blank=True, null=True)
    title_en = models.CharField('Заголовок на Английском', max_length=200, blank=True)
    title_jp = models.CharField('Заголовок на Японском', max_length=200, blank=True)
    title_ru = models.CharField('Заголовок на Русском', max_length=200, blank=True)
    description = models.TextField('Описание')

    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Эволюционировал от',
        null=True,
        blank=True,
        related_name='next_evolution'
    )

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE, null=True, verbose_name='Покемон')

    appeared_at = models.DateField('Время появления', default=timezone.now)
    disappeared_at = models.DateField('Время исчезновения', default=timezone.now)

    level = models.IntegerField('Уровень', default=1)
    health = models.IntegerField('Здоровье', default=100)
    strength = models.IntegerField('Сила', default=1)
    defence = models.IntegerField('Защита', default=1)
    stamina = models.IntegerField('Выносливость', default=1)

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'

    def __str__(self):
        return f'{self.pokemon.title} - {str(self.lat)} - {str(self.lon)}'
