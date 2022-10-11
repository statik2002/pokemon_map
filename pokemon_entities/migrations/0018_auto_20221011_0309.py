# Generated by Django 3.1.14 on 2022-10-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20221011_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок на Английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок на Японском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок на Русском'),
        ),
    ]
