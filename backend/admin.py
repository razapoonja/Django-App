from django.contrib import admin
from .models import Client, User, Location, TestStandard, Certificate, Product


admin.site.register(Client)
admin.site.register(User)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(Certificate)
admin.site.register(Product)


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin): 
#     list_display = ['client_name', 'client_type'] 
#     prepopulated_fields = {'client_name': ('client_type',)}


# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin): 
#     list_display = ['title', 'subject', 'created'] 
#     fields = ['subject', 'title', ('created',)]
#     list_filter = ['created', 'subject'] 
#     search_fields = ['title', 'overview'] 
#     prepopulated_fields = {'slug': ('title',)} 