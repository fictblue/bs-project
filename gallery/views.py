from django.shortcuts import render
from .models import Gallery


def gallery_list(request):
    galleries = Gallery.objects.all()
    category_filter = request.GET.get('category')
    
    if category_filter:
        galleries = galleries.filter(category=category_filter)
    
    context = {
        'galleries': galleries,
        'category_filter': category_filter,
    }
    return render(request, 'gallery/gallery_list.html', context)


def gallery_detail(request, pk):
    gallery = Gallery.objects.get(pk=pk)
    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery/gallery_detail.html', context)
