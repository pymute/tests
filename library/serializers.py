from rest_framework import serializers
from .models import AuthorModel, GenreModel, BookModel


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('name',)


class BookSerialziers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('name','author','year','genre','image','price','pages','desc')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('user','date_birth','dead','genre','image','bio')
