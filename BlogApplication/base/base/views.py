from django.shortcuts import render, get_object_or_404, redirect
from .models import *
def home_view(request):
    trending_articles = Article.objects.all()[:5]
    featured_recipes = Article.objects.all()
    testimonials = Testimonial.objects.all() 
    
    featured_recipes_with_time = []
    for article in featured_recipes:
        recipe = article.related_recipe if hasattr(article, 'related_recipe') else None
        if recipe:
            total_time = recipe.total_time()
            formatted_time = f"{total_time // 60} h {total_time % 60} min" if total_time >= 60 else f"{total_time} min"
        else:
            formatted_time = None
        featured_recipes_with_time.append({
            'article': article,
            'total_time': formatted_time,
        })

    categories = Category.objects.all()

    return render(request, 'home.html', {
        'trending_articles': trending_articles,
        'featured_recipes': featured_recipes_with_time,
        'categories': categories,
        'testimonials': testimonials,
    })


from django.db.models import Avg

from django.db.models import Avg

from django.db.models import Avg, Count

def article_list(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recipe = article.related_recipe if hasattr(article, 'related_recipe') else None
    tags = article.tags.all()
    context = {
        'article': article,
        'recipe': recipe,
    }

    if recipe:
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        comments = recipe.comments.all()
        average_rating = recipe.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

        # Calculate star counts and percentages
        total_reviews = recipe.ratings.count()
        star_counts = {star: 0 for star in range(1, 6)}
        ratings = recipe.ratings.values('rating').annotate(count=Count('rating'))
        for rating in ratings:
            star_counts[rating['rating']] = rating['count']

        star_percentages = {
            star: (count / total_reviews * 100) if total_reviews > 0 else 0
            for star, count in star_counts.items()
        }

        # Similar recipes and their ratings
        similar_recipes = Article.objects.prefetch_related('related_recipe').all()[:6]
        for similar_article in similar_recipes:
            related_recipe = similar_article.related_recipe
            if related_recipe:
                related_recipe.average_rating = related_recipe.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
                related_recipe.full_stars = range(int(related_recipe.average_rating))
                related_recipe.empty_stars = range(5 - int(related_recipe.average_rating))
                total_time = related_recipe.total_time()
                related_recipe.formatted_total_time = f"{total_time // 60} h {total_time % 60} min" if total_time >= 60 else f"{total_time} min"

        # Format total time for the main recipe
        total_time = recipe.total_time()
        formatted_total_time = f"{total_time // 60} h {total_time % 60} min" if total_time >= 60 else f"{total_time} min"

        # Update context with recipe details
        context.update({
            'total_time': formatted_total_time,
            'preparation_time': f"{recipe.preparation_time // 60} h {recipe.preparation_time % 60} min" if recipe.preparation_time >= 60 else f"{recipe.preparation_time} min",
            'cooking_time': f"{recipe.cooking_time // 60} h {recipe.cooking_time % 60} min" if recipe.cooking_time >= 60 else f"{recipe.cooking_time} min",
            'cost_estimate': f"{recipe.cost_estimate} MAD",
            'ingredients': ingredients,
            'formatted_preparation_description': recipe.format_preparation_description(),
            'similar_recipes': similar_recipes,
            'tags': tags,
            'comments': comments,
            'average_rating': average_rating,
            'full_stars': range(int(average_rating)),
            'empty_stars': range(5 - int(average_rating)),
            'total_reviews': total_reviews,
            'star_counts': star_counts,
            'star_percentages': star_percentages,
        })

    if request.method == 'POST':
        if recipe:
            comment_content = request.POST.get('comment')
            rating_value = request.POST.get('rating')

            if comment_content:
                Comment.objects.create(
                    user=request.user,
                    recipe=recipe,
                    content=comment_content
                )

            if rating_value:
                try:
                    rating_value = int(rating_value)
                    if 1 <= rating_value <= 5:
                        Rating.objects.create(
                            user=request.user,
                            recipe=recipe,
                            rating=rating_value
                        )
                except ValueError:
                    pass

            return redirect('article_detail', slug=article.slug)

    return render(request, 'article_list.html', context)
