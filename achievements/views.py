from django.shortcuts import render
from .models import Achievement


def achievement_list(request):
    achievements = Achievement.objects.all()
    category_filter = request.GET.get('category')
    
    if category_filter:
        achievements = achievements.filter(category=category_filter)
    
    context = {
        'achievements': achievements,
        'category_filter': category_filter,
    }
    return render(request, 'achievements/achievement_list.html', context)


def achievement_detail(request, pk):
    achievement = Achievement.objects.get(pk=pk)
    context = {
        'achievement': achievement,
    }
    return render(request, 'achievements/achievement_detail.html', context)
