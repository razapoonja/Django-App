from rest_framework import serializers
from ..models import Certificate, Client


class CertificateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Certificate
        fields = ['certificate_number', 'certificate_id', 'user_id', 'report_number', 'issue_date', 'standard_id', 'location_id', 'model_number']


class ClientSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Client
        fields = ['client_id', 'client_name', 'client_type']
