from django.contrib import admin
from .models import Member, Badge


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'real_name', 'role', 'status', 'created_at']
    list_filter = ['role', 'status', 'created_at']
    search_fields = ['nickname', 'real_name']
    filter_horizontal = ['badges']


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
