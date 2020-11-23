from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

#회원가입 제공 class
class signUpForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order=['username','password','password_check']
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password','password_check']

#로그인 제공 class
class signInForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password']