from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class register(forms.ModelForm):
    username = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter full name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
      
      
# 🔹 Login Form
class login_frm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )
    role = forms.ChoiceField(
        choices=[
            ('customer', 'Customer'),
            ('mechanic', 'Mechanic'),
            ('admin', 'Admin'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # 🔍 Custom validation
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password!")

        return cleaned_data