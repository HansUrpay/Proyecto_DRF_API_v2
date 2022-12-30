from rest_framework.viewsets import ModelViewSet
from .serializer import ServicesSerializer
from .models import Services
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ServicesView(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [AllowAny()]

    # def create(self, request):
    #     serializer = Services(data=request.data)
    #     if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     if self.request.method == "POST":
    #         return [AllowAny()]

