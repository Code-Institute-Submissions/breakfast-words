from django.contrib import admin
from .models import Book, Category
admin.site.register(Book)
admin.site.register(Category)

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
        'description'
        'category'
        'image_url'
    )
    ordering = ('sku',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
