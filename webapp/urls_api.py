from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'apiapp'

urlpatterns = [
    path('', auth_views.login_required(
            views.BookListApiView.as_view()), name='api-reading-list'),
    path('edit-book-<int:pk>', auth_views.login_required(
            views.BookUpdateApiView.as_view()), name='api-reading-detail')
]
