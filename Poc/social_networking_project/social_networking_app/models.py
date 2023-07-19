# models.py
from django.contrib.auth.models import User
from django.db import models

class Friendship(models.Model):
    requester = models.ForeignKey(User, related_name='friendship_requester', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='friendship_receiver', on_delete=models.CASCADE)
    status = models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
