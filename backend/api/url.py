from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [ 
    # path('products/', views.ProductListView.as_view(), name='product_list'), 
    # path('products/create/', views.ProductCreatelView.as_view(), name='product_create'),
    # path('products/<pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('products/update/<pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('products/delete/<pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    # path('certificates/', views.CertificateListView.as_view(), name='certificate_list'), 
    # path('certificates/create/', views.CertificateCreatelView.as_view(), name='certificate_create'),
    # path('certificates/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    # path('certificates/update/<pk>/', views.CertificateUpdateView.as_view(), name='certificate_update'),
    # path('certificates/delete/<pk>/', views.CertificateDeleteView.as_view(), name='certificate_delete'),

    # path('services/', views.ServiceListView.as_view(), name='service_list'), 
    # path('services/create/', views.ServiceCreatelView.as_view(), name='service_create'),
    # path('services/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    # path('services/update/<pk>/', views.ServiceUpdateView.as_view(), name='service_update'),
    # path('services/delete/<pk>/', views.ServiceDeleteView.as_view(), name='service_delete'),
]