from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [ 
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'), 
    path('clients/', views.ClientListView.as_view(), name='client_list'), 
]