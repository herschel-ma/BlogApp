from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings


class CustomPageNumber(PageNumberPagination):
    page_size = settings.PAGE_SIZE

    def get_paginated_response(self, data):
        return Response(
            OrderedDict([('count', self.page.paginator.count),
                         ('total_pages', self.page.paginator.num_pages),
                         ('count_items_on_page',
                          self.get_page_size(self.request)),
                         ('current_page', self.page.number),
                         ('next', self.get_next_link()),
                         ('previous', self.get_previous_link()),
                         ('per_page', self.page.paginator.per_page),
                         ('results', data)]))


class MyCustomPageNumber(PageNumberPagination):
    page_size = 2

    def get_from(self):
        return int((self.page.paginator.per_page * self.page.number) -
                   self.page.paginator.per_page + 1)

    def get_to(self):
        return self.get_from() + int(len(self.page.object_list)) - 1

    def get_paginated_response(self, data):

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'per_page': self.page.paginator.per_page,
            'from': self.get_from(),
            'to': self.get_to(),
            'results': data
        })
