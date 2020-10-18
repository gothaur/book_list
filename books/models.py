from django.db import models
from django.urls import (
    reverse,
)


class Author(models.Model):
    name = models.CharField(
        max_length=256,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ManyToManyField(
        Author,
    )
    image_link = models.URLField(
        null=True,
    )
    title = models.CharField(
        max_length=256,
    )
    isbn_number = models.CharField(
        max_length=17,
        null=True,
    )
    language = models.CharField(
        blank=True,
        null=True,
        max_length=8,
    )
    page_count = models.IntegerField(
        null=True,
    )
    partial_date = models.BooleanField(
        default=False,
    )
    published_date = models.DateField(
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('books:book-detail', kwargs={'book_id': self.pk})

    def __str__(self):
        return self.title
