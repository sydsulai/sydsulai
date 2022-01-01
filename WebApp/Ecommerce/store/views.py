from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def all_products(request):
    products_all = Product.objects.all()
    return render(request, 'store/home.html', {'products_all': products_all})


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'store/product/category.html', {'category': category, 'all_products': product})
