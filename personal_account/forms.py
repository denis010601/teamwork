from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class CastomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Выберете дату рождения",
    )
    class Meta:
        model = CastomUser
        fields = ['first_name', 'last_name', 'birth_date', 'username', 'password1', 'password1', 'profile_pic', 'mail']
