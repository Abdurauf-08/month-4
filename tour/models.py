from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тура')
    date = models.DateField(verbose_name='Дата тура')
    description = models.TextField(max_length=200, verbose_name='Описание')

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tour = models.OneToOneField(
        Tour,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE 
    )

    def __str__(self):
        return self.text





    
    

    

