from .views import RegisterAPI, LoginAPI
from django.urls import path
# from .views import dashboard, product, client, certificate, location, test_standard
from .views import index
from knox import views as knox_views

app_name = 'core'

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('', index, name='index'),
    # path('dashboard', dashboard, name='dashboard'),
    # path('product', product, name='product'),
    # path('client', client, name='client'),
    # path('certificate', certificate, name='certificate'),
    # path('location', location, name='location'),
    # path('test_standard', test_standard, name='test_standard'),
]
