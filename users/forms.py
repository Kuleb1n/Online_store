from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your password',
    }))

    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
