from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    book_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        if isinstance(item_data, int):
            book = get_object_or_404(Book, pk=item_id)
            total += item_data * book.price
            book_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'book': book,
            })
        else:
            book = get_object_or_404(Book, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
        total += quantity * book.price
        book_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
