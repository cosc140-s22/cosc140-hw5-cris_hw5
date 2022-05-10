from django.contrib import admin

from .models import Product
admin.site.register(Product)

from .models import ProductImage
admin.site.register(ProductImage)


