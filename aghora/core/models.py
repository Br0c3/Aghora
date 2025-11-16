from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

## CARTS
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creating_date = models.DateTimeField()
    # CartItems doivent être liés via ForeignKey dans CartItems, pas ici

class CartItems(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    part = models.ForeignKey('Parts', on_delete=models.CASCADE)
    quantity = models.IntegerField()

## INTERACTIONS

class OrdersComment(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment_text = models.TextField()

class PartComment(models.Model):
    id = models.AutoField(primary_key=True)
    part = models.ForeignKey('Parts', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment_text = models.TextField()

class LikedParts(models.Model):
    id = models.AutoField(primary_key=True)
    part = models.ForeignKey('Parts', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# ORDERS

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creating_date = models.DateTimeField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    # OrderItems doivent être liés via ForeignKey dans OrderItems, pas ici

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    part = models.ForeignKey('Parts', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

#PRODUCTS

class ImagesList(models.Model):
    id = models.AutoField(primary_key=True)
    part = models.ForeignKey('Parts', on_delete=models.CASCADE)

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image_list = models.ForeignKey('ImagesList', on_delete=models.CASCADE)
    image_url = models.ImageField()

class Parts(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=50)
    designation = models.CharField(max_length=128)
    price = models.CharField(default=0.0, max_length=10)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    sub_categorie = models.ForeignKey('SubCategorie', on_delete=models.CASCADE)

class SubCategorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)