# Generated by Django 3.1.14 on 2022-10-11 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0021_auto_20221011_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]