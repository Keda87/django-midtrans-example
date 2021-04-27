"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from payments.views import checkout_view, product_view, check_payment_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_view, name='index'),
    path('checkout/<product_id>', checkout_view, name='checkout'),
    path('payment-confirmation/<reference_id>', check_payment_info_view, name='payment-confirmation'),
]
