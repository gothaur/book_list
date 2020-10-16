from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)

from api.filters import (
    BookFilter,
)
from api.serializers import (
    BookSerializer,
)

from books.models import (
    Book,
)


class BookAPIView(ListAPIView):

    filterset_class = BookFilter
    permission_classes = [
        AllowAny,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

