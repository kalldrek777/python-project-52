from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control'}
                                 ))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control'}
                                ))
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}
                               ))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}
                                ))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}
                                ))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control'}
                                 ))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control'}
                                ))
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}
                               ))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}
                                ))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}
                                ))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Имя пользователя'}
                               ))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'}
                               ))
