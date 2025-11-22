from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author')  # Admin panelinde görüntülenecek sütunlar
    search_fields = ('title', 'description','author')  # Arama yapılacak alanlar
    list_filter = ('author',)  # Filtreleme seçenekleri
    row_id_fields = ('author',)  # Yabancı anahtar alanları için hızlı seçim