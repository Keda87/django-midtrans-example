PAYMENT_STATUS = {
    'pending': 'Belum Dibayar',
    'settlement': 'Telah Dibayar',
    'expire': 'Pembayaran Melebihi Batas Transaksi',
    'cancel': 'Anda Batalkan',
    'deny': 'Pembayaran Ditolak'
}

DUMMY_PRODUCTS = [
    {
        'id': 'prd-1',
        'name': 'Don\'t make me think',
        'image_url': 'https://sensible.com/divi/wp-content/uploads/2020/09/DMMT-cover-262x300.png',
        'price': 30_000
    },
    {
        'id': 'prd-2',
        'name': 'REMOTE',
        'image_url': ('https://basecamp.com/assets/books/remote/'
                      'remote-cover-aadeb20bf72bc28d49a49d2433e731d36c8a255f9d496880a5224e1ce0006577.png'),
        'price': 67_000
    },
    {
        'id': 'prd-3',
        'name': 'The Lean Startup',
        'image_url': ('https://i.gr-assets.com/images/S/'
                      'compressed.photo.goodreads.com/books/1333576876l/10127019.jpg'),
        'price': 89_000
    },
]
