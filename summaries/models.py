from django.db import models

class Summary(models.Model):
    title = books.models.ForeignKey(default=(), max_length=254, null=False, blank=False)
    author_surname = books.models.ForeignKey(max_length=254, null=False, blank=False)
    author_firstname = books.models.ForeignKey(max_length=254, null=False, blank=False)
    date_summary = models.DateField()
    content_summary = models.TextField()
    category = books.models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image = models.ForeignKey(null=True, blank=True)

    def __str__(self):
        return self.name
