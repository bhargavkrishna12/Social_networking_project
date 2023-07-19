# social_networking_app/urls.py

# urls.py
from django.urls import path
from django.contrib import admin
from social_networking_app.views import UserSignupView,UserSigninView, UserSearchView, FriendRequestView, FriendRequestActionView, FriendListView, PendingFriendRequestListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('signin/', UserSigninView.as_view(), name='user-signin'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/', FriendRequestView.as_view(), name='friend-request'),
    path('friend-request/action/', FriendRequestActionView.as_view(), name='friend-request-action'),
    path('friends/', FriendListView.as_view(), name='friend-list'),
    path('pending-requests/', PendingFriendRequestListView.as_view(), name='pending-friend-requests'),
]

