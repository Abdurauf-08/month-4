from django.urls import path 
from . import views

urlpatterns = [
    path('product_list/', views.product_list_view, name='product_list_view'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail_view')

]