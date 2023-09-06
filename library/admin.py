from django.contrib import admin
from .models import AuthorModel, GenreModel, BookModel

admin.site.register(GenreModel)
admin.site.register(BookModel)
admin.site.register(AuthorModel)
