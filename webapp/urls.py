from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = 'webapp'

urlpatterns = [
    path('api/readinglist', auth_views.login_required(
            views.BookListApiView.as_view()), name='api-reading-list'),
    path('api/edit-book-<int:pk>', auth_views.login_required(
            views.BookUpdateApiView.as_view()), name='api-reading-detail'),
    path('login/', auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='webapp/login.html',
            success_url=reverse_lazy('webapp:books_listing')),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='webapp/logout.html'
    ), name='logout'),
    path('add/', auth_views.login_required(views.BookAddView.as_view()),
         name='book-add'),
    path('delete-book-<int:pk>',
         auth_views.login_required(views.BookDeleteView.as_view()),
         name='book-delete'),
    path('edit-book-<int:pk>',
         auth_views.login_required(views.BookEditView.as_view()),
         name='book-edit'),
    path('', auth_views.login_required(views.BooksListView.as_view()),
         name='books_listing')
]
