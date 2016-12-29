from django.contrib import admin
from lr6.models import BookModel
from lr6.models import OrderModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(OrderModel)
