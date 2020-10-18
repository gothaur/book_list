from django.urls import (
    path,
)
from api.views import (
    AuthorAPIView,
    BookAPIView,
    RetrieveAuthorView,
)

app_name = 'api'
urlpatterns = [

    path('authors/', AuthorAPIView.as_view()),
    path('authors/<int:pk>', RetrieveAuthorView.as_view()),
    path('books/', BookAPIView.as_view()),
]
