from django.contrib import admin
from .models import Blog, Category


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'content',
        'summery',
        'author',
    )


admin.site.register(Category)
