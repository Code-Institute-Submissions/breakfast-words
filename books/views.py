from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    """ A view to show all books, including sorting and search queries """

    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/products_detail.html', context)
