from django.urls import (
    path,
)
from api.views import (
    BookAPIView,
)

app_name = 'api'
urlpatterns = [
    path('books/', BookAPIView.as_view()),
]
