from django import forms
from .models import User, UploadedFile

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'mobile', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
