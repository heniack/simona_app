from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=False,
        help_text='',
        validators=[],
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    first_name = forms.CharField(
        label='Nombre',
        max_length=150,
        required=False,
        help_text='',
        validators=[],
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=150,
        required=False,
        help_text='',
        validators=[],
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password1 = forms.CharField(
        label=_('Contraseña'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        validators=[validate_password],
        help_text=_('Tu contraseña debe contener al menos 8 caracteres y no puede ser toda numérica.'),
    )
    password2 = forms.CharField(
        label=_('Confirme su contraseña'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        validators=[validate_password],
        help_text=_('Tu contraseña debe ser la misma que ingresaste arriba.')
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)