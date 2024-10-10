from django.shortcuts import render,redirect
from . models import orders,orderedItem
from products . models import products
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = orders.objects.get_or_create(
        owner = customer,
        oreder_status = orders.CART_STAGE
    ) 
    context = {'cart':cart_obj}

    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        print(product_id)
        cart_obj,created = orders.objects.get_or_create(
            owner = customer,
            oreder_status = orders.CART_STAGE
        ) 
        product = products.objects.get(pk=product_id)
        ordered_item,created = orderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj,

        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')


def remove_items_from_cart(request,pk):
    item = orderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = orders.objects.get(
                owner = customer,
                oreder_status = orders.CART_STAGE
            ) 
            if order_obj:
                order_obj.oreder_status = orders.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_msg = "Your order is processed. Your item will be delivered within 4 days."
                messages.success(request,status_msg)
            else:
                status_msg = "Unable to processed. No items in cart"
                messages.error(request,status_msg)
        except Exception as e:
            status_msg = "Unable to processed. No items in cart"
            messages.error(request,status_msg)
    return redirect('cart')

@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = orders.objects.filter(owner=customer).exclude(oreder_status=orders.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'orders.html',context)