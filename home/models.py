from django.db import models

# Create your models here.

# category

class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

# Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.ImageField(upload_to="product_imgs/",null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# product image
class ProductImage(models.Model):
    
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product_imgs/",null=True)

    def __str__(self):
        return self.Product.title


class Enquiry(models.Model):


    Product=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField(default=0)
    email =  models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    requirment = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Subscribtion(models.Model):

    email =  models.CharField(max_length=50)


    def __str__(self):
        return self.email
    

class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email =  models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
        