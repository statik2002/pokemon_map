from django.urls import path

from pokemon_entities import views

app_name = 'pokemon_entities'

urlpatterns = [
    path('show_pokemon/<int:pokemon_id>', views.show_pokemon, name='show_pokemon'),
]
