# Generated by Django 3.1.14 on 2022-10-10 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_pokemon_evolve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='evolve',
            new_name='previous_evolution',
        ),
    ]
