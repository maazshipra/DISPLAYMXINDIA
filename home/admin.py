from django.contrib import admin
from .models import Category, Product,Enquiry,Subscribtion,Contact, ProductImage


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Enquiry)
admin.site.register(Subscribtion)
admin.site.register(Contact)
admin.site.register(ProductImage)