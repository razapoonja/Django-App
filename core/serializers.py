from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'username', 'email', 'password', 'company', 'job_title', 'office_phone', 'cell_phone', 'appellation')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['first_name'], validated_data['last_name'], validated_data['username'], validated_data['email'], validated_data['password'])

        return user