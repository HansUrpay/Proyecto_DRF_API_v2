from rest_framework import viewsets
from .models import PaymentUser, ExpiredPayment
from .serializer import PaymentUserSerializer, ExpiredPaymentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class PaymentUserView(viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    # pagination_class = Pagination_own
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["payment_date", "expiration_date"]
    # throttle_scope = 'payments'

    def create(self, request):
        serializer = PaymentUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class ExpiredPaymentView(viewsets.ModelViewSet):
    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    # pagination_class = Pagination_own
    # throttle_scope = 'all'

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [IsAuthenticated()]
    #     if self.request.method == "POST":
    #         return [IsAdminUser]
