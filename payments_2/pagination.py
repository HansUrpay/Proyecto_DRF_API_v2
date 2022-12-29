from rest_framework.pagination import PageNumberPagination

class PaymentUserPagination(PageNumberPagination):
    page_size = 100
    page_query_param = "page"


class ExpiredPaymentPagination(PageNumberPagination):
    page_size = 100
    page_query_param = "page"

