from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class EmailForm(forms.Form):

    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
    to_email = forms.EmailField()

    class Meta:
        fields = '__all__'


class RegistrationForm(UserCreationForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1',
                  'password2')
