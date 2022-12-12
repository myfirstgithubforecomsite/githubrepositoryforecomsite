from django.contrib import admin

# Register your models here.
from shop.models import *
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)
class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','price','stock','image','available']
    list_editable = ['price','image','available']
admin.site.register(products,prodadmin)
