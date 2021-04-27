import uuid

import midtransclient
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from payments.constants import DUMMY_PRODUCTS, PAYMENT_STATUS

MIDTRANS_CORE = midtransclient.CoreApi(
    is_production=not settings.DEBUG,
    server_key=settings.MIDTRANS['SERVER_KEY'],
    client_key=settings.MIDTRANS['CLIENT_KEY'],
)

MIDTRANS_SNAP = midtransclient.Snap(
    is_production=not settings.DEBUG,
    server_key=settings.MIDTRANS['SERVER_KEY'],
    client_key=settings.MIDTRANS['CLIENT_KEY'],
)


def product_view(request):
    ctx = {
        'products': DUMMY_PRODUCTS
    }

    return render(request, 'index.html', ctx)


def checkout_view(request, product_id):
    try:
        product = [x for x in DUMMY_PRODUCTS if x.get('id') == product_id][0]
    except KeyError:
        raise Http404

    resp = MIDTRANS_CORE.charge({
        "payment_type": "bank_transfer",
        "transaction_details": {
            "order_id": uuid.uuid4().hex,  # mocked order id
            "gross_amount": product.get('price')
        },
        "bank_transfer": {
            "bank": "bca"
        },
        'metadata': {
            'product_id': product_id
        },
    })

    ctx = {
        'transaction_id': resp.get('transaction_id'),
        'amount': resp.get('gross_amount'),
        'status': PAYMENT_STATUS[resp.get('transaction_status')],
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
        'product': product,
    }

    return render(request, 'payment.html', ctx)


def check_payment_info_view(request, reference_id):
    resp = MIDTRANS_CORE.transactions.status(reference_id)

    product_id = resp.get('metadata').get('product_id')

    try:
        product = [x for x in DUMMY_PRODUCTS if x.get('id') == product_id][0]
    except KeyError:
        raise Http404

    ctx = {
        'transaction_id': reference_id,
        'amount': resp.get('gross_amount'),
        'status': PAYMENT_STATUS[resp.get('transaction_status')],
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
        'product': product,
    }

    return render(request, 'payment.html', ctx)
