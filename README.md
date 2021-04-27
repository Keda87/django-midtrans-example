# django-midtrans-example


### DISCLAIMER
Project ini hanya sebatas proof of concept dan belum siap untuk skala production, karena banyak hal yang perlu diperhatikan terkait security dan akan diserahkan ke masing-masing untuk dikembangkan lebih lanjut.

---

### Cara penggunaan:
Copy file `.env.example` ke `.env` dan update sesuai dengan credential masing-masing, kemudian jalankan perintah berikut.
```
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver
```

Simulasi pembayaran bisa dilakukan melalui [midtrans payment sandbox](https://simulator.sandbox.midtrans.com/bca/va/index).

### TODO:
- [x] Core API dengan BCA Virtual Account
- [ ] Core API menggunakan opsi pembayaran lainnya
- [ ] Snap API
- [ ] Webhook Success
