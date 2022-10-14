from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    image = models.ImageField('Изображение покемона', upload_to='pokemons_images/', blank=True, null=True)
    title_en = models.CharField('Заголовок на Английском', max_length=200, blank=True)
    title_jp = models.CharField('Заголовок на Японском', max_length=200, blank=True)
    title_ru = models.CharField('Заголовок на Русском', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)

    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Эволюционировал от',
        null=True,
        blank=True,
        related_name='next_evolutions'
    )

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    pokemon = models.ForeignKey(
        'Pokemon',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Покемон',
        related_name='pokemon'
    )

    appeared_at = models.DateField('Время появления', default=timezone.now)
    disappeared_at = models.DateField('Время исчезновения', default=timezone.now)

    level = models.IntegerField('Уровень')
    health = models.IntegerField('Здоровье')
    strength = models.IntegerField('Сила')
    defence = models.IntegerField('Защита')
    stamina = models.IntegerField('Выносливость')

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'

    def __str__(self):
        return f'{self.pokemon.title_ru} - {str(self.lat)} - {str(self.lon)}'
