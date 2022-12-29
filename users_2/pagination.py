from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 100
    page_query_param = "page"