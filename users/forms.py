from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class UserForm(UserCreationForm):
    phone = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username',
                  'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'phone', 'photo')

