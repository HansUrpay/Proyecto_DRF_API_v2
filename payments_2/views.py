from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentUser, ExpiredPayment
from .serializer import PaymentUserSerializer, ExpiredPaymentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import PaymentUserPagination, ExpiredPaymentPagination

# Create your views here.
class PaymentUserView(viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = PaymentUserPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["payment_date", "expiration_date"]
    # throttle_scope = 'payments'

    def create(self, request):
        serializer = PaymentUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            payment_date = serializer.data.get("payment_date")
            expiration_date = serializer.data.get("expiration_date")
            if expiration_date < payment_date:
                datos = {
                    "payment_user_id": serializer.data.get("id"),
                    "penalty_fee_amount": 0.2*float(serializer.data.get("amount")),
                    "user_id": serializer.data.get("user_id"),
                    "service_id": serializer.data.get("service_id"),
                    "amount": serializer.data.get("amount"),
                }

                serializer_2 = ExpiredPaymentSerializer(data=datos)
                if serializer_2.is_valid():
                    serializer_2.save()
                    return Response({
                        "ok":True,
                        "message":"Datos agregados",
                        "data_1":serializer.data,
                        "message":"Datos agregados en Pagos Expirados",
                        "data_2":serializer_2.data
                }, status=status.HTTP_201_CREATED)

            return Response({
                "ok":True,
                "message":"Datos creados",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ExpiredPaymentView(viewsets.ModelViewSet):
    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    pagination_class = ExpiredPaymentPagination
    # throttle_scope = 'all'

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [IsAuthenticated()]
    #     if self.request.method == "POST":
    #         return [IsAdminUser]
