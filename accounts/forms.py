from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field
    is_admin = forms.BooleanField(required=False, label='Admin')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_admin']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_admin']:
            user.is_staff = True
        if commit:
            user.save()
        return user

