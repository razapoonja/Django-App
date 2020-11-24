# def dashboard(request):
#     return render(request, "solarpv/dashboard.html")

# def client(request):
#     return render(request, "solarpv/client.html")

# def product(request):
#     return render(request, "solarpv/product.html")

# def location(request):
#     return render(request, "solarpv/location.html")

# def certificate(request):
#     return render(request, "solarpv/certificate.html")

# def test_standard(request):
#     return render(request, "solarpv/test_standard.html")


from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.shortcuts import render


def index(request):
    return render(request, "solarpv/index.html") 


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)