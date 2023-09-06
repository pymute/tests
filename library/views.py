from django.shortcuts import render
from rest_framework import generics
from .models import GenreModel, AuthorModel, BookModel
from .serializers import GenreSerializers, AuthorSerializer, BookSerialziers
from config.permissions import AdminPermission, AuthorPermission

# Create your views here.

class ListGenreAPIView(generics.ListCreateAPIView):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializers
    permission_classes = (AdminPermission,)

# class UpadteBookAPIView(generics.UpdateAPIView):
#     queryset = GenreModel.objects.all()
#     serializer_class = GenreSerializers
#     permission_classes = (AdminPermission,)

class ListBookByAuthorAPIView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerialziers
    permission_classes = (AuthorPermission,)

    def get_queryset(self):
        user = self.request.user
        author = AuthorModel.objects.get(user=user)
        return BookModel.objects.filter(author=author.id)

# class DetailBookAPIView(generics.DestroyAPIView):
#     queryset = GenreModel.objects.all()
#     serializer_class = GenreSerializers
#     permission_classes = (AdminPermission,)