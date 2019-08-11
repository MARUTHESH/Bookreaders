from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author_name', 'publication', 'publication',
                    'summary', 'status', 'user', 'created_on', 'updated_on']
    list_filter = ['status', 'user']
