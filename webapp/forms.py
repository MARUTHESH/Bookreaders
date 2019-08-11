from django import forms
from django.apps import apps
BookModel = apps.get_model('webapp', 'BookModel')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['book_name', 'author_name', 'publication',
                  'year_of_publication', 'summary', 'status']
