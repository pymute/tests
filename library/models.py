from django.db import models
from account.models import CustomUser
from datetime import datetime

class GenreModel(models.Model):
    name = models.CharField(max_length=25, default='')

    class Meta:
        db_table = 'book_genre'

    def __str__(self):
        return self.name

class AuthorModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_birth = models.DateField(default=datetime.now)
    dead = models.BooleanField(default=False)
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE)
    date_dead = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='image/')
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.first_name

    class Meta:
        db_table = 'author'


class BookModel(models.Model):
    name = models.CharField(default='', max_length=20)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(default=1924)
    genre = models.ForeignKey(GenreModel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField(default=0)
    pages = models.PositiveSmallIntegerField(default=4)
    desc = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'