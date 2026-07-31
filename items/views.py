import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    return render(request, 'items/index.html')

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.currency.lower() == 'eur':
        public_key = settings.STRIPE_PUBLIC_KEY_EUR
    else:
        public_key = settings.STRIPE_PUBLIC_KEY

    return render(request, 'items/item_detail.html', {
        'item': item,
        'public_key': public_key
    })

def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.currency.lower() == 'eur':
        stripe.api_key = settings.STRIPE_SECRET_KEY_EUR
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency.lower(),
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': item.price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + '/success.html',
            cancel_url=settings.DOMAIN + '/cancel.html',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()
    if not items:
        return JsonResponse({'error': 'Order is empty'}, status=400)

    currency = items[0].currency.lower()

    if currency == 'eur':
        stripe.api_key = settings.STRIPE_SECRET_KEY_EUR
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY

    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        })

    session_kwargs = {
        'line_items': line_items,
        'mode': 'payment',
        'success_url': settings.DOMAIN + '/success.html',
        'cancel_url': settings.DOMAIN + '/cancel.html',
    }

    if order.tax:
        session_kwargs['automatic_tax'] = {'enabled': True}

    if order.discount:
        coupon_data = {'name': order.discount.name}
        if order.discount.percent_off:
            coupon_data['percent_off'] = order.discount.percent_off
        elif order.discount.amount_off:
            coupon_data['amount_off'] = order.discount.amount_off
            coupon_data['currency'] = currency

        try:
            coupon = stripe.Coupon.create(**coupon_data)
        except stripe.error.InvalidRequestError:
            # Если купон уже существует, пробуем получить его или создаем с уникальным именем
            coupon_data['name'] = f"{coupon_data['name']}_{order.id}"
            coupon = stripe.Coupon.create(**coupon_data)
        session_kwargs['discounts'] = [{'coupon': coupon.id}]

    try:
        checkout_session = stripe.checkout.Session.create(**session_kwargs)
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)def success(request):
    return render(request, 'items/success.html')

def cancel(request):
    return render(request, 'items/cancel.html')
