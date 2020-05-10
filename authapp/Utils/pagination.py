from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPaginator(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_secure_link(self, link_method):
        url = getattr(super(MyPaginator, self), link_method)()
        if isinstance(url, str):
            return url

    def get_paginated_response(self, data, **kwargs):
        try:
            return Response({
                'links': {
                    'next': self.get_secure_link('get_next_link'),
                    'previous': self.get_secure_link('get_previous_link')
                },
                'count': kwargs.get('count', self.page.paginator.count),
                'flights': data
            })
        except Exception as e:
            return Response({"detail":
                            "Oops!! Something wrong with pagination."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomPaginator(MyPaginator):

    def __init__(self, max_page_size=None):
        self.max_page_size = self.page_size = max_page_size or 30
        super(CustomPaginator, self).__init__()

    def get_paginated_response(self, data, **kwargs):
        try:
            return Response({
                'links': {
                    'next': self.get_secure_link('get_next_link'),
                    'previous': self.get_secure_link('get_previous_link')
                },
                'count': kwargs.get('count', self.page.paginator.count),
                'result': data
            })
        except Exception as e:
            return Response({"detail":
                            "Oops!! Something wrong with pagination."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
