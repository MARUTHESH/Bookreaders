from django.views import generic
from django.apps import apps
from django.urls import reverse_lazy
from django.http import Http404
from . import forms
from rest_framework import generics
from .serializers import BookModelSerializer

BookModel = apps.get_model('webapp', 'BookModel')

# Web Views Start


class BooksListView(generic.ListView):
    '''
        Reading List View returns the list of books created by the logedin user
    '''
    template_name = 'webapp/book_list.html'
    model = BookModel
    context_object_name = 'books_list'

    def get_queryset(self):
        queryset = super(BooksListView, self).get_queryset()
        # Filters the queryset based on the GET request
        if 'filterby' in self.request.GET:
            queryset = queryset.filter(user=self.request.user)
            if self.request.GET['filterby'] == 'All':
                return queryset
            return queryset.filter(status=self.request.GET['filterby'])
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BookAddView(generic.CreateView):
    '''
        Book Add view is used to add the book to readinglist
    '''
    template_name = 'webapp/add_book.html'
    # CreatView using formclass
    form_class = forms.AddBookForm
    success_url = reverse_lazy('webapp:books_listing')

    def form_valid(self, form):
        # adds the user as currently logedin user
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookEditView(generic.UpdateView):
    '''
        Book Edit view is used to edit the information of already added book.
    '''
    template_name = 'webapp/edit_book.html'
    # UpdateView using model and fields
    model = BookModel
    fields = ['book_name', 'author_name', 'publication',
              'year_of_publication', 'summary', 'status']
    success_url = reverse_lazy('webapp:books_listing')


class BookDeleteView(generic.DeleteView):
    template_name = 'webapp/delete_book.html'
    model = BookModel
    success_url = reverse_lazy('webapp:books_listing')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Checks wether currently logedin users book is only deleted or not
        if not obj.user == self.request.user:
            raise Http404('You are not allowed to delete this object')
        return obj

#  Web Views End

# Api Views Start


class BookListApiView(generics.ListCreateAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        return BookModel.objects.filter(user=self.request.user)


class BookUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        return BookModel.objects.filter(user=self.request.user)

#  Api Views End
