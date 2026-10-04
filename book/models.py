from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=255)
    author = models.CharField(verbose_name='Автор', max_length=100)
    genre = models.CharField(verbose_name='Жанр', max_length=100)
    publication_year = models.IntegerField(verbose_name='Год публикаци')
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    pages = models.IntegerField(verbose_name='Количество страниц')
    rating = models.FloatField(verbose_name='Рейтинг')
    description = models.TextField(verbose_name='Описание')
    publisher = models.CharField(verbose_name='Издательство', max_length=100)
    is_available = models.BooleanField(verbose_name='Доступна ли книга в продаже')



    def __str__(self):
        return self.title 



    

