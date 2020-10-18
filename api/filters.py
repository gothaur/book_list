import django_filters

from books.models import (
    Book
)


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='name__icontains')
    language = django_filters.CharFilter(lookup_expr='iexact')
    published_date__gt = django_filters.DateFilter(
        field_name='published_date', lookup_expr='gt'
    )
    published_date__lt = django_filters.DateFilter(
        field_name='published_date', lookup_expr='lt'
    )

    class Meta:
        model = Book
        fields = [
            'author',
            'language',
            'title',
        ]
