from django.shortcuts import render
from .models import Lore


def lore_list(request):
    lores = Lore.objects.all()
    category_filter = request.GET.get('category')
    
    if category_filter:
        lores = lores.filter(category=category_filter)
    
    context = {
        'lores': lores,
        'category_filter': category_filter,
    }
    return render(request, 'lore/lore_list.html', context)


def lore_detail(request, pk):
    lore = Lore.objects.get(pk=pk)
    context = {
        'lore': lore,
    }
    return render(request, 'lore/lore_detail.html', context)
