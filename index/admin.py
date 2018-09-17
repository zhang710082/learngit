from django.contrib import admin
from .models import *
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_filter = ['goodsType']
    search_fields = ['title']
admin.site.register(User)
admin.site.register(GoodsType)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(CartInfo)