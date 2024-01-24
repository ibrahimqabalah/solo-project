from django.urls import path
from . import views
urlpatterns = [
    path('',views.index ),
    path('register',views.register ),
    path('login',views.login ),
    path('success',views.main ),
    path('logout',views.logout ),
    path('products/', views.products, name='products'),
    path('products/new/', views.new_product, name='new_product'),
    path('products/<int:product_id>/', views.product_details, name='product_details'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('cart/delete/<int:cart_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('purchase/', views.purchase, name='purchase'),
    path('about_us',views.about ),
]
