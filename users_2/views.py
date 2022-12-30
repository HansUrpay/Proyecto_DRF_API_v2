from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth.models import User
from .pagination import UserPagination
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination