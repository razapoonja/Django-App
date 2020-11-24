from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [ 
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'), 
    path('certificates/create/', views.CertificateCreatelView.as_view(), name='certificate_create'),
    path('certificates/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    path('certificates/update/<pk>/', views.CertificateUpdateView.as_view(), name='certificate_update'),
    path('certificates/delete/<pk>/', views.CertificateDeleteView.as_view(), name='certificate_delete'),
]