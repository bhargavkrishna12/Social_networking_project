# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Friendship

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email','username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserSigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name']

class FriendshipSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Friendship
        fields = ['requester', 'receiver', 'status', 'created_at']
