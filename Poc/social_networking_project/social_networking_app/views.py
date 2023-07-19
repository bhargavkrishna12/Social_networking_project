# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSignupSerializer, UserSigninSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Friendship
from .serializers import UserSerializer, FriendshipSerializer
from rest_framework.permissions import IsAuthenticated
class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSigninView(APIView):
    def post(self, request):
        serializer = UserSigninSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            print(user)
            if user:
                login(request, user)
                return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_keyword = request.query_params.get('search_keyword', '')
        users = User.objects.filter(Q(email__icontains=search_keyword) | Q(first_name__icontains=search_keyword) | Q(last_name__icontains=search_keyword))[:10]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FriendRequestView(APIView):
    def post(self, request):
        requester = request.user
        receiver_id = request.data.get('receiver_id')
        if Friendship.objects.filter(requester=requester, status='pending').count() >= 3:
            return Response({'message': 'You cannot send more than 3 friend requests within a minute.'}, status=status.HTTP_400_BAD_REQUEST)
        if Friendship.objects.filter(requester=requester, receiver_id=receiver_id).exists():
            return Response({'message': 'Friend request already sent to this user.'}, status=status.HTTP_400_BAD_REQUEST)
        receiver = User.objects.get(pk=receiver_id)
        friendship = Friendship(requester=requester, receiver=receiver)
        friendship.save()
        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FriendRequestActionView(APIView):
    def post(self, request):
        friendship_id = request.data.get('friendship_id')
        action = request.data.get('action')
        friendship = Friendship.objects.get(pk=friendship_id)
        if action == 'accept':
            friendship.status = 'accepted'
            friendship.save()
        elif action == 'reject':
            friendship.status = 'rejected'
            friendship.save()
        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FriendListView(APIView):
    def get(self, request):
        user = request.user
        friends = Friendship.objects.filter(Q(requester=user, status='accepted') | Q(receiver=user, status='accepted'))
        serializer = FriendshipSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PendingFriendRequestListView(APIView):
    def get(self, request):
        user = request.user
        pending_requests = Friendship.objects.filter(receiver=user, status='pending')
        serializer = FriendshipSerializer(pending_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
