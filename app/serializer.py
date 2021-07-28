from rest_framework import serializers
from .models import Task01, Task02
from .models import Task03

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class Task01Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H%M", read_only=True)

    class Meta:
        model = Task01
        fields = ('id', 'title', 'created_at', 'code')


class Task02Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H%M", read_only=True)

    class Meta:
        model = Task02
        fields = ('id', 'title1', 'created_at')
        read_only_fields = ['title1']


class Task03Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H%M", read_only=True)

    class Meta:
        model = Task03
        fields = ('id', 'name', 'contents', 'created_at')
