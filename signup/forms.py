from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    address = forms.CharField(max_length=100, help_text='Required.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(required=False, help_text='Optional. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'address',
                  'birth_date', 'password1', 'password2')
