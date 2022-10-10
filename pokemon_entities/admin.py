from django.contrib import admin

from .models import Pokemon, PokemonEntity


class PokemonAdmin(admin.ModelAdmin):
    ...


class PokemonEntityAdmin(admin.ModelAdmin):
    ...


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonEntity, PokemonEntityAdmin)
