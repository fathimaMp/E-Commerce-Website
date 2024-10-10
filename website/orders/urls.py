from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('cart/',views.show_cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove/<pk>/',views.remove_items_from_cart,name='remove'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.show_orders,name='orders'),



]
