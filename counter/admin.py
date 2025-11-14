from django.contrib import admin
from .models import DownloadCounter

@admin.register(DownloadCounter)
class DownloadCounterAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
