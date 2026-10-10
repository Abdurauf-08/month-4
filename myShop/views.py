from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serial_number = product.serial_number 
    comments = product.comments.all()

    context ={
        'product' : product, 
        'serial_number' : serial_number,
        'comments' : comments,
    }
    return render(request, 'product_detail.html',context)

