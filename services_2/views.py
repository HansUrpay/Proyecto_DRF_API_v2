from rest_framework import viewsets
from .serializer import ServicesSerializer
from .models import Services
# Create your views here.

class ServicesView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # throttle_classes = 'all'