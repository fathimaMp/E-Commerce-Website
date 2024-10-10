from django.contrib import admin
from orders.models import orderedItem,orders

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "oreder_status",
    ]
    search_fields = (
        "owner",
        "id",
    )
admin.site.register(orders,OrderAdmin)