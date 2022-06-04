from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def store(request):
    products = Product.objects.all()
    paginator = Paginator(products,8,orphans = 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
    }
    return render(request,'app_store/store.html',context)

def categoryfetchItem(request,slug):

    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        context = {
        'products': products
    }
        return render(request,'app_store/store.html',context)
    else:
        messages.warning(request,'Product is not available')
        return render(request,'app_store/store.html')

        
def productDetails(request,cat_slug,prod_slug):

    if(Category.objects.filter(slug=cat_slug)):
        if (Product.objects.filter(slug=prod_slug)):
            products = Product.objects.filter(slug=prod_slug).first()
            context = {
                'single_product': products
            }
        return render(request,'app_store/product_details.html',context)

def SearchProduct(request):
    search = request.GET['search_item']
    products = Product.objects.filter(name__icontains=search).order_by('-name')
    if products !=None and products !='':
        return render(request,'app_store/search.html',context={'object_list':products})
    else:
        messages.warning(request,'Product Not Found')
        return redirect('store')