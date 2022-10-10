from django.urls import path

from pokemon_entities import views

urlpatterns = [
    path('pokemon/<pokemon_id>/', views.show_pokemon, name='pokemon'),
]