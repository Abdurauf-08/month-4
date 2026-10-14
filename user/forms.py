from django import forms
from user.models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=100)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, initial='@gmail.com')
    phone_number = forms.CharField(required=True, initial='+996', max_length=15)
    photo = forms.ImageField(required=True)
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'photo',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=True)
            user.email = self.cleaned_data('email')
            if commit:
                user.save()
            return user



