from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'event_date', 'created_at']
    list_filter = ['category', 'event_date', 'created_at']
    search_fields = ['title', 'caption']
