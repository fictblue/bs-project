from django.contrib import admin
from .models import Lore


@admin.register(Lore)
class LoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_occurred', 'created_at']
    list_filter = ['category', 'date_occurred']
    search_fields = ['title', 'content']
