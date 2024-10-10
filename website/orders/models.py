from django.db import models
from products.models import products
from customers.models import customers


# Create your models here.

# create cart models
class orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_PROCESSED,"ORDER_PROCESSED"),
                    (ORDER_DELIVERED,"ORDER_DELIVERED"),
                    (ORDER_REJECTED,"ORDER_REJECTED"))
    oreder_status = models.IntegerField(choices = STATUS_CHOICE,default = CART_STAGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(customers,on_delete = models.SET_NULL,null = True, related_name = 'added_orders')
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.user.username)

class orderedItem(models.Model):
    product = models.ForeignKey(products,related_name = "added_order", on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 1)
    owner = models.ForeignKey(orders,on_delete = models.SET_NULL, null = True, related_name = 'added_items')