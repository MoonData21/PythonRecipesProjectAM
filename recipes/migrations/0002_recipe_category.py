# Generated by Django 5.1.6 on 2025-07-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="category",
            field=models.CharField(
                choices=[
                    ("main", "Main Dish"),
                    ("side", "Side Dish"),
                    ("dessert", "Dessert"),
                    ("breakfast", "Breakfast"),
                    ("snack", "Snack"),
                ],
                default="main",
                max_length=20,
            ),
        ),
    ]
