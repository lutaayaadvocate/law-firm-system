from django.contrib import admin
from .models import Draft

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')