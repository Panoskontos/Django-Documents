from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect

# Read
# List


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'dishes/products.html', context)

# Single


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'dishes/product.html', context)


# Create
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
            # or redirect success

    context = {
        'form': form,
    }
    return render(request, 'dishes/create-product.html', context)
