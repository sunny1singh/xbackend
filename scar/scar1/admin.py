from django.contrib import admin
from scar1.models import snacks,DairyItems,Fruits,Vegetables,Babycare

# Register your models here.
class snacksAdmin(admin.ModelAdmin):
    list_display=['image','name','price','off']


class DairyItemsAdmin(admin.ModelAdmin):
    list_display=['image','name','price','off']


class FruitsAdmin(admin.ModelAdmin):
    list_display=['image','name','price','off']


class VegetablesAdmin(admin.ModelAdmin):
    list_display=['image','name','price','off']


class BabycareAdmin(admin.ModelAdmin):
    list_display=['image','name','price','off']


admin.site.register(snacks,snacksAdmin)
admin.site.register(DairyItems,DairyItemsAdmin)
admin.site.register(Fruits,FruitsAdmin)
admin.site.register(Vegetables, VegetablesAdmin)
admin.site.register(Babycare, BabycareAdmin)