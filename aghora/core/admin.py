from django.contrib import admin
from .models import Cart, CartItems, OrdersComment, PartComment,LikedParts,Order,OrderItems,Status, ImagesList,Categorie, Group, Images, Parts, SubCategorie


admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(OrdersComment)
admin.site.register(PartComment)
admin.site.register(LikedParts)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Status)
admin.site.register(ImagesList)
admin.site.register(Categorie)
admin.site.register(Group)
admin.site.register(Images)
admin.site.register(Parts)
admin.site.register(SubCategorie)