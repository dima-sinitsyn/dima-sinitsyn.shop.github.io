from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
    username = forms.CharField()
    password = forms.CharField()
    
   
    
    # username = forms.CharField(
    #     label = 'Имя пользователя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = forms.CharField(
    #     label = 'Пароль пользователя',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль'})
    # )

class UserRegistartionForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name", 
            "username",
            "gender_yours",
            "telephone",
            "adress_living_city",
            "adress_living2",
            "adress_living3",
            "flat",
            "email",
            "password1",
            "password2",
        )
        
        
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    gender_yours = forms.CharField(required=False)
    telephone = forms.CharField(required=False)
    adress_living_city = forms.CharField(required=False)
    adress_living2 = forms.CharField(required=False)
    adress_living3 = forms.CharField(required=False)
    flat= forms.CharField(required=False)
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "gender_yours",
            "telephone",
            "adress_living_city",
            "adress_living2",
            "adress_living3",
            "flat",
            "email",
            )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    gender_yours = forms.CharField(required=False)
    telephone = forms.CharField(required=False)
    adress_living_city = forms.CharField(required=False)
    adress_living2 = forms.CharField(required=False)
    adress_living3 = forms.CharField(required=False)
    flat = forms.CharField(required=False)
    email = forms.CharField()