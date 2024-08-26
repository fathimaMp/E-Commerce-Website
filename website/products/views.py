from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

#list all products
def list_products(request):
    return render(request,'list_products.html')

#details of single product
def product_details(request):
    return render(request,'product_detail.html')