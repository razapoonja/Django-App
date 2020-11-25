from rest_framework import generics
from ..models import Certificate
from .serializers import CertificateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['certificate_number']


class CertificateDetailView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer


class CertificateCreatelView(generics.CreateAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer


class CertificateUpdateView(generics.UpdateAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer


class CertificateDeleteView(generics.DestroyAPIView):
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer