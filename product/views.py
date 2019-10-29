from django.shortcuts import render
from .models import Product,Order,OrderItem
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
def add_to_cart(request, **kwargs):
    product= Product.objects.filter(id=kwargs.get('item_id',"")).first()
    order_item,status=OrderItem.objects.get_or_create(product=product)
    user_order,status=Order.objects.get_or_create(buyer=request.user)
    user_order.items.add(order_item)
    return redirect('product_list')
def get_pending_order(request):
    order=Order.objects.filter(buyer=request.user)
    if order.exists():
        return order[0]
    return 0
def order_details(request):
    existing_order=get_pending_order(request)
    context={'order':existing_order }
    return render(request,'product/cart.html',context)
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        
    return redirect('order_summary')
