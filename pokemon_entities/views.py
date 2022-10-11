import folium
import json

from django.db.models import Q
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from django.core.exceptions import ObjectDoesNotExist

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities_query = Q(appeared_at__gte=localtime()) and Q(disappeared_at__lte=localtime())
    pokemons_entity = PokemonEntity.objects.filter(pokemon_entities_query)
    pokemons_on_page = Pokemon.objects.all()

    for pokemon in pokemons_entity:
        add_pokemon(
            folium_map,
            pokemon.lat,
            pokemon.lon,
            pokemon.pokemon.image.path
        )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    query = Q(appeared_at__gte=localtime()) and Q(disappeared_at__lte=localtime()) and Q(pokemon_id=pokemon_id)
    pokemons_entities = PokemonEntity.objects.filter(query)
    if not pokemons_entities:
        raise Http404('Нет таких покемонов')
    current_pokemon = pokemons_entities.first().pokemon

    pokemon = {
        'image': current_pokemon.image,
        'title_en': current_pokemon.title_en,
        'title_jp': current_pokemon.title_jp,
        'title_ru': current_pokemon.title_ru,
        'description': current_pokemon.description,
        'next_evolution': current_pokemon.next_evolutions.all().first(),
        'previous_evolution': current_pokemon.previous_evolution
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon['image'].path,
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
