from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.shortcuts import redirect

def product_list(request):
    products=Product.objects.order_by('price')
    return render(request, 'product/product_list.html', {'products': products})
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product= form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product/product_new.html', {'form': form})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_details.html', {'product': product})
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.check=request.user
    return redirect('product_detail', pk=product.pk)


    


