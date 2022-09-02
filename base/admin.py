from django.contrib import admin

# Register your models here.

from .models import Order, Item, Profile, Coupon

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Item)
