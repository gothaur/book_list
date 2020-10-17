from django import forms
from django.core.validators import (
    URLValidator
)

from books.models import (
    Book,
)


class BookForm(forms.ModelForm):

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
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Data w formacie YYYY-MM-DD lub YYYY',
            }
        )
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

    def clean_published_date(self):
        fixed_date = self.cleaned_data['published_date']
        if len(fixed_date) <= 5:
            fixed_date = f"{fixed_date[:4]}-01-01"
            self.modified = True
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
                'class': 'form-control',
                'placeholder': 'Autor',
            }
        ),
    )
    publisher = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Wydawca',
            }
        ),
    )
    subject = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Temat',
            }
        ),
    )
    isbn = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Numer ISBN',
            }
        ),
    )
    lccn = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Numer LCCN',
            }
        ),
    )
    oclc = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Numer OCLC',
            }
        ),
    )
