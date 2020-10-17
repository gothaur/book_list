from django.http import HttpResponseRedirect
from django.urls import (
    reverse_lazy
)
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)

from books.forms import (
    AddBookForm,
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
    form_class = AddBookForm

    def form_valid(self, form):

        author = form.cleaned_data.get('author', '')
        image_link = form.cleaned_data.get('image_link', '')
        title = form.cleaned_data.get('title', '')
        isbn_number = form.cleaned_data.get('isbn_number', '')
        language = form.cleaned_data.get('language', '')
        partial_date = form.cleaned_data.get('partial_date', '')
        page_count = form.cleaned_data.get('page_count', '')
        published_date = form.cleaned_data.get('published_date', '')

        try:
            Book.objects.get(
                author__iexact=author,
                image_link=image_link,
                title__iexact=title,
                isbn_number=isbn_number,
                language=language,
                page_count=page_count,
            )

        except Book.DoesNotExist:
            Book.objects.create(
                author=author,
                image_link=image_link,
                title=title,
                isbn_number=isbn_number,
                language=language,
                page_count=page_count,
                partial_date=partial_date,
                published_date=published_date,
            )

        return HttpResponseRedirect(reverse_lazy('books:book-list'))


class UpdateBookView(UpdateView):
    form_class = AddBookForm
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
        context['form'] = ImportBookForm(self.request.GET)

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
