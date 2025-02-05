from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# List & Search
def product_list(request):
    query = request.GET.get("q", "")
    products = Product.objects.filter(name__icontains=query)
    return render(request, "store/product_list.html", {"products": products, "query": query})

# Create
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "store/product_form.html", {"form": form})

# Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "store/product_form.html", {"form": form})

# Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "store/product_confirm_delete.html", {"product": product})
