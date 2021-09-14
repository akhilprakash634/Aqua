from django.urls import path
from.import views

urlpatterns = [
    path('cartdetails', views.cart_detail, name="cartdetails"),
    path('add/<int:product_id>/', views.add_cart, name="addcart"),
    path('cart_deriment/<int:product_id>/', views.min_cart, name="cart_decriment"),
    path('remove/<int:product_id>/', views.cart_delete, name="remove"),

]