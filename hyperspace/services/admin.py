from django.contrib import admin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured','slug')  # Admin panelinde görüntülenecek sütunlar
    prepopulated_fields = {'slug': ('title',)}  # Slug alanını title alanından otomatik doldur
    search_fields = ('title', 'description')  # Arama yapılacak alanlar
    list_filter = ('is_featured',)  # Filtreleme seçenekleri