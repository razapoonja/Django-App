from django.contrib import admin
from .models import Client, User, Location, TestStandard, Certificate, Product


admin.site.register(User)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(Product)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin): 
    list_display = ['client_name', 'client_type'] 
    list_filter = ['client_name'] 
    search_fields = ['client_name'] 


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin): 
    list_display = ['certificate_number', 'report_number', 'model_number'] 
    list_filter = ['certificate_number'] 
    search_fields = ['certificate_number'] 

