from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    title = models.CharField('Наименование покемона', max_length=200)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемон'

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('pokemon', kwargs={'pk': self.pk})
