from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)

from api.filters import (
    BookFilter,
)
from api.serializers import (
    AuthorSerializer,
    BookSerializer,
)

from books.models import (
    Author,
    Book,
)


class AuthorAPIView(ListAPIView):

    permission_classes = [
        AllowAny,
    ]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookAPIView(ListAPIView):

    filterset_class = BookFilter
    permission_classes = [
        AllowAny,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RetrieveAuthorView(RetrieveAPIView):
    permission_classes = [
        AllowAny,
    ]

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
