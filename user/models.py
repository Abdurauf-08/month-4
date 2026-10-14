from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15)
    GENDER = (
        ('М', 'М'),
        ('Ж', 'Ж')
    )
    gender = models.CharField(max_length=100, 
                              choices=GENDER,
                              default='М')
    def __str_(self):
        return self.username 
    

    
