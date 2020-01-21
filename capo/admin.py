from django.contrib import admin
from .models import Guitar, Accessories, Apparel

# Register your models here.

admin.site.register(Guitar)

admin.site.register(Accessories)

admin.site.register(Apparel)