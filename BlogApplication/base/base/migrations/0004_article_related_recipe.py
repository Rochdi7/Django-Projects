# Generated by Django 5.1.4 on 2024-12-23 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_ingredient_remove_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='related_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='base.recipe'),
        ),
    ]
