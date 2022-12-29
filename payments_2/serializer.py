from rest_framework import serializers
from .models import PaymentUser, ExpiredPayment

class PaymentUserSerializer(serializers.Serializer):
    class Meta:
        model = PaymentUser
        fields = '__all__'

    def validate(self, data):
        amount = data.get("amount")
        if amount < 0:
            raise serializers.ValidationError("El monto no puede ser negativo")
        return data

class ExpiredPaymentSerializer(serializers.Serializer):
    class Meta:
        model = ExpiredPayment
        fields = '__all__'
     