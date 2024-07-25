from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published', 'view_count')
    list_filter = ('title',)
    search_fields = ('title', 'is_published')
