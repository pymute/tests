from django.urls import path
from .views import ListGenreAPIView, ListBookByAuthorAPIView

urlpatterns = [
    path('genre/', ListGenreAPIView.as_view()),
    path('book_by_author/', ListBookByAuthorAPIView.as_view())

]
