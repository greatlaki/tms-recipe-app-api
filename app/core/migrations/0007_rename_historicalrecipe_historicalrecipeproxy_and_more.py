# Generated by Django 4.2 on 2023-05-22 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_recipeproxy_historicalrecipe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalRecipe',
            new_name='HistoricalRecipeProxy',
        ),
        migrations.AlterModelOptions(
            name='historicalrecipeproxy',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical recipe proxy', 'verbose_name_plural': 'historical recipe proxys'},
        ),
    ]
