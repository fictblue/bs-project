from django.contrib import admin
from .models import AIMemory, AIConversation


@admin.register(AIMemory)
class AIMemoryAdmin(admin.ModelAdmin):
    list_display = ['key', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['key', 'content']


@admin.register(AIConversation)
class AIConversationAdmin(admin.ModelAdmin):
    list_display = ['user_message', 'created_at']
    list_filter = ['created_at']
