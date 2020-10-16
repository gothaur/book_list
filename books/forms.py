from django import forms
from django.core.validators import (
    URLValidator
)

from books.models import (
    Book,
)


class BookForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tytuł',
            }
        ),
        label='',
        required=False,
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
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Data w formacie YYYY-MM-DD lub YYYY',
            }
        )
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


class ImportBookForm(forms.Form):

    title = forms.CharField(max_length=256, required=False)
    author = forms.CharField(max_length=256, required=False)
    publisher = forms.CharField(max_length=256, required=False)
    subject = forms.CharField(max_length=1024, required=False)
    isbn = forms.CharField(max_length=17, required=False)
    lccn = forms.CharField(max_length=32, required=False)
    oclc = forms.CharField(max_length=32, required=False)
