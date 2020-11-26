#Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True, label='Nombres')
    last_name = forms.CharField(max_length=140, required=True, label='Apellidos')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos'
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs['class'] = 'input100'