from django.db import models

class Anketa(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.title
