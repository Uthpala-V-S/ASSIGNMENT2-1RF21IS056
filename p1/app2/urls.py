from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register_customer'),
    path('products/<str:customer_id>/', views.products_page, name='products_page'),
    path('open_savings_account/<str:customer_id>/', views.open_savings_account, name='open_savings_account'),
    path('open_mf_account/<str:customer_id>/', views.open_mf_account, name='open_mf_account'),
    path('open_loan_account/<str:customer_id>/', views.open_loan_account, name='open_loan_account'),
]