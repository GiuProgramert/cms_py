from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, FeaturedContent

def home(request):
    return redirect("login")

@login_required
def home_view(request):
    # Fetch recent articles
    recent_articles = Article.objects.order_by('-published_date')[:5]
    
    # Fetch featured content
    featured_content = FeaturedContent.objects.filter(is_active=True).order_by('priority')
    
    # Any additional context
    context = {
        'recent_articles': recent_articles,
        'featured_content': featured_content,
    }
    
    # Corrected template path
    return render(request, 'home.html', context)

