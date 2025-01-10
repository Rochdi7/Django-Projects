from django.contrib import admin
from .models import Article, Tag, Category, Recipe, Comment, Ingredient, RecipeIngredient, Rating, Testimonial

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_featured')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ['ingredient']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'preparation_time', 'cooking_time', 'cost_estimate', 'is_featured')
    search_fields = ('title', 'preparation_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeIngredientInline]

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name', 'location', 'content')
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Rating)
admin.site.register(Testimonial, TestimonialAdmin)
