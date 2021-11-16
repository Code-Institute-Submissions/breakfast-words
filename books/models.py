from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    title = models.CharField(default=(), max_length=254, null=True, blank=True)
    author_surname = models.CharField(max_length=254, null=True, blank=True)
    author_firstname = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateField()
    isbn = models.IntegerField()
    book_format = models.CharField(max_length=254, null=True, blank=True)
    pages = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
