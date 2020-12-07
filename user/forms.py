#Django
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
#Models
from .models import Profile

class ProfileForm(forms.ModelForm):
    """Formulario para actualizar datos personales"""
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['username'].widget.attrs['readonly'] = True

    def clean_email(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.email
        else:
            return self.cleaned_data['email']
    
    def clean_username(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.username
        return self.cleaned_data['username']


class ProfileUpdateForm(forms.ModelForm):
    """Formulario para actualizar foto de perfil"""
    class Meta:
        model = Profile
        fields = ['image']