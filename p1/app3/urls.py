from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_figure, name='convert_figure'),
    path('print_cheque/', views.print_cheque, name='print_cheque'),
]