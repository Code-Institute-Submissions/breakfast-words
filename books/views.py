from django.shortcuts import render
from .models import Product

def all_books(request):
    """ A view to show all books, including sorting and search queries """

    books = Book.objects.all()

    context = {
        'books': books,
    }

return render(request, 'books/books.html', context)