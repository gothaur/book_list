from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)

from books.forms import (
    BookForm,
    ImportBookForm,
    SearchBookForm,
)

from books.models import (
    Book,
)

from books.services import (
    get_book
)


class BookListView(ListView):

    context_object_name = 'books'
    http_method_names = ['get', 'post']
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchBookForm(self.request.GET)

        return context

    def get_queryset(self):

        title = self.request.GET.get('title', '')
        author = self.request.GET.get('author', '')
        language = self.request.GET.get('language', '')
        date_from = self.request.GET.get('date_from', '')
        date_to = self.request.GET.get('date_to', '')

        qs = Book.objects.filter(
            title__icontains=title,
            author__icontains=author,
            language__icontains=language,
        )

        if date_from != '' and date_from is not None:
            qs = qs.filter(published_date__gte=date_from)

        if date_to != '' and date_to is not None:
            qs = qs.filter(published_date__lte=date_to)

        return qs


class AddBookView(CreateView):
    template_name = 'books/add_book.html'
    form_class = BookForm


class UpdateBookView(UpdateView):
    form_class = BookForm
    pk_url_kwarg = 'book_id'
    template_name = 'books/update_book.html'
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class ImportBookView(ListView):

    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'books/import_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ImportBookForm()

        return context

    def get_queryset(self):

        title = self.request.GET.get('title', '')
        author = self.request.GET.get('author', '')
        publisher = self.request.GET.get('publisher', '')
        subject = self.request.GET.get('subject', '')
        isbn = self.request.GET.get('isbn', '')
        lccn = self.request.GET.get('lccn', '')
        oclc = self.request.GET.get('oclc', '')

        try:
            qs = get_book(title, author, publisher, subject, isbn, lccn, oclc)
        except KeyError:
            qs = []
        return qs
