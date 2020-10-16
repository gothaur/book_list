from django.urls import path

from books.views import (
    AddBookView,
    BookDetailView,
    BookListView,
    ImportBookView,
    UpdateBookView,
)

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('add/', AddBookView.as_view(), name='add-book'),
    path('detail/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('edit/<int:book_id>/', UpdateBookView.as_view(), name='book-edit'),
    path('import/', ImportBookView.as_view(), name='import-book'),
]
