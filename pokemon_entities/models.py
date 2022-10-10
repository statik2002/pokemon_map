from django.db import models
from django.urls import reverse
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField('Наименование покемона', max_length=200)
    image = models.ImageField('Изображение покемона', upload_to='pokemons_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('pokemon:show_pokemon/', kwargs={'pk': self.pk})


class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE, null=True)

    appeared_at = models.DateField(default=timezone.now)
    disappeared_at = models.DateField(default=timezone.now)

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
