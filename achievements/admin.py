from django.contrib import admin
from .models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'recipient', 'date_achieved']
    list_filter = ['category', 'date_achieved']
    search_fields = ['title', 'recipient']
