# from rest_framework import serializers
# from ..models import Product, Certificate, Service


# class ProductSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = Product
#         fields = ['model_number', 'product_name', 'cell_technology', 'cell_manufacturer', 'number_cells', 'number_cells_series', 'number_cells_strings', 'number_diodes', 'product_length', 'product_width', 'product_weight', 'superstate_type', 'superstate_manufacturer', 'substrate_type', 'substrate_manufacturer', 'frame_type', 'frame_adhesive', 'encapsulate_type', 'encapsulate_manufacturer', 'junction_box_type', 'junction_box_manufacturer']


# class CertificateSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = Certificate
#         fields = ['certificate_number', 'certificate_id', 'user_id', 'report_number', 'issue_date', 'standard_id', 'location_id', 'model_number']


# class ServiceSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = Service
#         fields = ['service_id', 'service_name', 'description', 'fi_required', 'fi_frequency', 'standard_id']