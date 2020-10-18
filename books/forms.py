from django import forms
from django.core.validators import (
    URLValidator
)
import re

from books.models import (
    Book,
)


class AddBookForm(forms.ModelForm):

    modified = False

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tytuł',
            }
        ),
        label='',
    )

    author = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Autor',
            }
        ),
        label='',
        required=False,
    )

    isbn_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Numer ISBN',
            }
        ),
        label='',
        required=False,
    )

    page_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Liczba stron',
            }
        ),
        label='',
        required=False,
    )

    image_link = forms.URLField(
        label='',
        required=False,
        validators=[URLValidator],
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Link do okładki',
            }
        ),
    )

    published_date = forms.CharField(
        label='Data publikacji',
        initial=None,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Data w formacie YYYY-MM-DD lub YYYY',
            }
        ),
    )

    partial_date = forms.BooleanField(
        widget=forms.HiddenInput(),
        initial=False,
        required=False,
    )

    language = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Język publikacji',
            }
        ),
        label='',
    )

    class Meta:
        model = Book
        fields = '__all__'

    def clean_image_link(self):
        fixed_url = self.cleaned_data['image_link']
        if fixed_url == '':
            fixed_url = 'https://www.midi24.pl/skorki/v2018/brak-okladki.svg'

        return fixed_url

    def clean_isbn_number(self):
        isbn = self.cleaned_data['isbn_number']

        if len(isbn) == 0 or len(isbn) == 13 or len(isbn) == 10:
            return isbn
        else:
            msg = "Numer ISBN zawiera 13 lub 10 cyfr"
            self.add_error('isbn_number', msg)

    def clean_published_date(self):
        fixed_date = self.cleaned_data['published_date']
        if 3 < len(fixed_date) <= 5:
            fixed_date = f"{fixed_date[:4]}-01-01"
            self.modified = True

        if fixed_date == '':
            fixed_date = None

        return fixed_date

    def clean(self):
        cd = super().clean()
        if self.modified:
            cd['partial_date'] = True


class SearchBookForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Tytuł',
            }
        ),
        label='',
        required=False,
    )
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Autor',
            }
        ),
        label='',
        required=False,
    )
    language = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Język publikacji',
            }
        ),
        label='',
        required=False,
    )
    date_from = forms.DateField(
        label='Data publikacji od',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-3',
                'type': 'date',
            }
        ),
        required=False,
    )
    date_to = forms.DateField(
        label='Data publikacji do',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-3',
                'type': 'date',
            }
        ),
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        date__gte = cleaned_data.get("date_from")
        date__lte = cleaned_data.get("date_to")

        if date__gte and date__lte and date__lte < date__gte:
            msg = "Data 'od' nie może być większa od daty 'do'"
            self.add_error('date_from', msg)
            self.add_error('date_to', msg)


class ImportBookForm(forms.Form):

    title = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Tytuł',
            }
        ),
    )
    author = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Autor',
            }
        ),
    )
    publisher = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Wydawca',
            }
        ),
    )
    subject = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Temat',
            }
        ),
    )
    isbn = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Numer ISBN',
            }
        ),
    )
    lccn = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Numer LCCN',
            }
        ),
    )
    oclc = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Numer OCLC',
            }
        ),
    )

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']

        if len(isbn) == 0 or len(isbn) == 13 or len(isbn) == 10:
            return isbn
        else:
            msg = "Numer ISBN zawiera 13 lub 10 cyfr"
            self.add_error('isbn', msg)

    def clean_oclc(self):
        oclc = self.cleaned_data['oclc']

        if re.match(r'^ocm\d{8}$', oclc) \
                or re.match(r'^ocn\d{9}$', oclc) \
                or re.match(r'^on\d{10,}$', oclc) \
                or len(oclc) < 1:
            return oclc

        msg = "Niepoprawny numer OCLC"
        self.add_error('oclc', msg)
