from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author_surname',
        'author_firstname',
        'price',
        'publisher',
        'date',
        'isbn',
        'book_format',
        'pages',
        'sku',
        'description',
        'category',
        'image_url',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
