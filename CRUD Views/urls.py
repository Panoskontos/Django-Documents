from django.urls import include, path
from .views import *

urlpatterns = [
    # CRUD Views
    # Read
    path('products', products, name="products"),
    path('products/<str:pk>', product, name="product"),
    path('create-product', create_product, name="create-product"),
]
