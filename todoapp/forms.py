from django import forms

class Signupform(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder':'username','id':'username'})
    )
    email = forms.EmailField(
        label = "Email",
        max_length = 50,
        widget=forms.EmailInput(attrs={'placeholder':'email','id':'email'})
    )
    password1 = forms.CharField(
        label = "Password",
        max_length = 50,
        widget=forms.PasswordInput(attrs={'placeholder':'password','id':'password1'})
    )
    password2 = forms.CharField(
        label = "Confirm Password",
        max_length = 50,
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','id':'password2'})
    )
class loginform(forms.Form):
    username = forms.CharField(
        label = 'username',
        max_length = 50,
        widget=forms.TextInput(attrs={'placeholder':'username','id':'username'})
    )
    password = forms.CharField(
        label = 'password',
        max_length = 50,
        widget=forms.PasswordInput(attrs={'placeholder':'password','id':'password'})
    )
class inpform(forms.Form):
    Title = forms.CharField(
        label = 'Add new...',
        max_length = 100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder':'Add new...','id': 'Title'})
    )
    Date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date','id': 'date'}))
class editform(forms.Form):
    Title = forms.CharField(
        label = 'Edit-Title',
        max_length = 100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Edit-Title','id':'edtitle'})
    )
    date = forms.CharField(
        label = 'Edit-Date',
        max_length = 100,
        widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Edit-Date','id':'eddate'})

    )

    
    