from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect

from .models import Category, Product
from .forms import ProductForm

PRODUCT_PER_PAGE = 8


def paginate_catalog(queryset, request):
    paginator = Paginator(queryset, PRODUCT_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_products_categories():
    products = Product.objects.all()
    categories = Category.objects.all()
    return products, categories


def homepage(request):
    template = "products_list.html"
    products, categories = get_products_categories()
    page_obj = paginate_catalog(products, request)
    context = {
        "products": products,
        "categories": categories,
        "page_obj": page_obj,
        "card": False,
    }
    return render(request, template, context)


def contacts(request):
    template = "contacts.html"
    _, categories = get_products_categories()
    context = {
        "categories": categories,
    }
    if request.method == "POST":
        user_name = request.POST.get("name")
        phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        filename = f"сообщение_от_{user_name}.txt"
        message = f"Пользователь: {user_name} (телефон: {phone}) оставил сообщение '{user_message}'"
        file = open(filename, "w", encoding="utf-8")
        file.write(message)
        file.close()
    return render(request, template, context)


def product_detail(request, pk):
    template = "products_list.html"
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "card": True,
    }
    return render(request, template, context)


def product_create(request):
    template = "product_create.html"
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect("catalog:product_detail", pk=product.pk)
        return render(request, template, {"form": form})
    form = ProductForm()
    return render(request, template, {"form": form})
