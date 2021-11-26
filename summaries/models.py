from django.db import models

from books.models import Book


class Summary(models.Model):
    title = models.ForeignKey("Books", max_length=254, null=False, blank=False, default="")
    author_surname = models.ForeignKey("Books", max_length=254, null=False, blank=False, default="")
    author_firstname = models.ForeignKey("Books", max_length=254, null=False, blank=False, default="")
    date_summary = models.DateField()
    content_summary = models.TextField()
    image = models.ForeignKey("Books", max_length=254, null=False, blank=False, default="")

    def __str__(self):
        return self.name
