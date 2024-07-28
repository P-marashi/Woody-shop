from django.contrib import admin
from .models import CategoryModel

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'description', 'deleted_at')
    search_fields = ('name',)
