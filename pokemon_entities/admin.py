from django.contrib import admin

from .models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    ...


admin.site.register(Pokemon, PokemonAdmin)
