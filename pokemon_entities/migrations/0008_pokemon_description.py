# Generated by Django 3.1.14 on 2022-10-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20221010_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Нет описания', verbose_name='Описание'),
        ),
    ]
