from rest_framework import generics
from ..models import Certificate, Client
from .serializers import CertificateSerializer, ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['certificate_number']

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer