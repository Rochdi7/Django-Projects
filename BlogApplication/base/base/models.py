from django.db import models
from django.contrib.auth.models import User
import re
# Article model for general blog articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', default='default.jpg')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='articles')
    related_recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')

    def __str__(self):
        return self.title


# Tag model for categorizing articles
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# Category model for recipe categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

import re
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    preparation_time = models.PositiveIntegerField(help_text="Time in minutes", default=0)
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes", default=0)
    cost_estimate = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost in local currency", default=0.00)
    preparation_description = models.TextField(help_text="Detailed preparation steps", blank=True)

    def total_time(self):
        return self.preparation_time + self.cooking_time

    def format_preparation_description(self):
        formatted_description = re.sub(
            r'(Étape \d+)', 
            r'<br><br><strong class="etape">\1</strong><br><br>', 
            self.preparation_description
        )
        return formatted_description.strip()

    def __str__(self):
        return self.title


# Ingredient model for storing ingredient details
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredients/', blank=True, null=True)

    def __str__(self):
        return self.name

# RecipeIngredient model to associate ingredients with recipes and their quantities
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, help_text="e.g., 1.5 morceau, 0.5 verre")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient} for {self.recipe}"

# Comment model for storing comments on recipes
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe}"


# Rating model for users to rate recipes
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Ratings from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Ensure a user can rate a recipe only once

    def __str__(self):
        return f"Rating of {self.rating} by {self.user} for {self.recipe}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    location = models.CharField(max_length=150, verbose_name="Localisation")
    content = models.TextField(verbose_name="Témoignage")
    image = models.ImageField(upload_to='testimonials/', verbose_name="Photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")

    def __str__(self):
        return f"{self.name} - {self.location}"