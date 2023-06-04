from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'name'}))
    email = forms.EmailField(label='E-mail', max_length=100,
                           widget=forms.EmailInput(attrs={'class': 'e-mail'}))
    text = forms.CharField(label='Комментарий',
                           widget=forms.Textarea(attrs={'class': 'text', 'rows': 5}))