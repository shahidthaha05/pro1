from django.db import models
from django.contrib.auth.models import User





class Size(models.Model):
    name = models.CharField(max_length=10)  # Small, Medium, Large

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_id=models.TextField()
    name=models.TextField()
    base_price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()
    sizes = models.ManyToManyField(Size)  # Allow multiple size selection
    quantity = models.PositiveIntegerField(default=1)

    def calculate_price(self, quantity):
        return self.base_price * quantity  # Price increases with quantity

    def __str__(self):
        return self.name





class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1) 




    def total_price(self):
        return self.product.offer_price * self.quantity 


class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    



class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    shipping_address = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)



class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    # Other fields like price, date, etc.
