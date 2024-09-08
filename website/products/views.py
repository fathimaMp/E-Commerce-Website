from django.shortcuts import render
from . models import products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = products.objects.order_by('priority')[:4]
    latest_products = products.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

#list all products
def list_products(request):
    page  = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = products.objects.order_by('priority')
    product_paginator = Paginator(product_list,2)
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request,'products.html',context)

#details of single product
def product_details(request,pk):
    product = products.objects.get(pk=pk)
    context = {'products':product}
    return render(request,'product_detail.html',context)