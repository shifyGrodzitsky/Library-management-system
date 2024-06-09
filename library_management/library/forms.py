from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    address = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    phone = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    date_of_birth = forms.DateField(label='',required=True, widget=forms.DateInput(attrs={'placeholder': 'Date Of Birth'}))
