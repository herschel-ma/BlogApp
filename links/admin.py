from django.contrib import admin
from .models import Links, Category


# Register your models here.
@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'category',
        'show',
        'thumbnail_url',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
