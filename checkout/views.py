from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51JjPYqBBi58M3Z5kI1r10PKJeqNMPkNYvuEmP09TK7XoqOus62RBUEgo4sX4SKTvOqCZEcbGvUq1y9z6dx07expM00f5GdS2Uz',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
