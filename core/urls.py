from .views import RegisterAPI, LoginAPI
from django.urls import path
from .views import index, testing_and_certification
from knox import views as knox_views

app_name = 'core'

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('', index, name='index'),
    path('testing_and_certification', testing_and_certification, name='testing_and_certification'),
]
