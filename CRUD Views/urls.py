from django.urls import include, path
from .views import *

urlpatterns = [
    # CRUD Views
    # Read
    path('products', products, name="products"),
    path('products/<str:pk>', product, name="product"),
    path('create-product', create_product, name="create-product"),
    path('update-product/<str:pk>', update_product, name="update-product"),
    path('delete-product/<str:pk>', delete_product, name="delete-product"),

]
