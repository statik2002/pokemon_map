from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    title = models.CharField('Наименование покемона', max_length=200)
    image = models.ImageField('Изображение покемона', upload_to='media/pokemons_images', blank=True, null=True)

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

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'

    def __str__(self):
        return f'{str(self.lat)} - {str(self.lon)}'
