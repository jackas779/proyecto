#Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
            'first_name': 'Nombre',
            'last_name': 'Apellido'
        }

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email ya existente!")
       return self.cleaned_data


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in iter(self.fields):
            self.fields[field].widget.attrs['class'] = 'input100'