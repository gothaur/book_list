"""book_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
