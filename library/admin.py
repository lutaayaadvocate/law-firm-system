from django.contrib import admin
from .models import LibraryDocument

@admin.register(LibraryDocument)
class LibraryDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title',)