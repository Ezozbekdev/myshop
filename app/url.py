from django.urls import path
from .views import My_list, Creat_Product, DeleteProduct, main, LoginPage, Register, contact
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('log-out/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', LoginPage.as_view(), name='login'),

    path('contact/', contact, name='contact'),
    path('create/', Creat_Product.as_view(), name='product_create'),
    path('list/', My_list.as_view(), name='list'),
    path('product-delete/<int:pk>/', DeleteProduct.as_view(), name='Delete'),

    path('', main, name='main'),
]

