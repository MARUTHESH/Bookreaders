from rest_framework import serializers
from .models import BookModel
from django.db import IntegrityError
from django.core import exceptions


class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
                        view_name='apiapp:api-reading-detail')

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        try:
            return super(BookModelSerializer, self).create(validated_data)
        except IntegrityError as e:
            raise exceptions.NotAcceptable(str(e))

    class Meta:
        model = BookModel
        fields = ['id', 'book_name', 'author_name', 'publication',
                  'year_of_publication', 'summary', 'status', 'url']
