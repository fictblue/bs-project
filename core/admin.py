from django.contrib import admin
from .models import DailyQuote

@admin.register(DailyQuote)
class DailyQuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'created_at']
    list_filter = ['created_at']
