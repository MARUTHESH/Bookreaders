from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('To Read', 'To Read'),
    ('Reading', 'Reading'),
    ('Completed', 'Completed')
]


class BookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255, blank=False)
    author_name = models.CharField(max_length=255, blank=False)
    publication = models.CharField(max_length=255, blank=False)
    year_of_publication = models.PositiveIntegerField(
                                default=datetime.today().year)
    summary = models.TextField(max_length=2500, blank=False)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.book_name)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
