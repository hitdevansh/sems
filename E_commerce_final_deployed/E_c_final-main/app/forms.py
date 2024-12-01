from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer,STATE_CHOICES

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class': 'form-control'}))
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),
                    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
                    'current-password','autofocus':True,'class':'form-control'}))
    
    new_password1 = forms.CharField(label=_("New Password"),
                    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
                    'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"),
                    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
                    'new-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'),max_length=254,required=True, widget=forms.EmailInput(attrs={'autocomplete':'email','class': 'form-control'}))


class MySetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"),
                    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
                    'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"),
                    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
                    'new-password','class':'form-control'}))
    

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'locality':forms.TextInput(attrs={'class':'form-control'}),
                   'city':forms.TextInput(attrs={'class':'form-control'}),
                   'state': forms.Select(attrs={'class': 'form-control'}),
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


# class ContactUsForm(forms.Form):
#     name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     subject = forms.CharField(label='Subject', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
