from django import forms
from . models import contactModel

class contactForms(forms.ModelForm):
    first_name = forms.CharField(max_length= 55, required=False, widget=(forms.TextInput(attrs={
        'id': 'contactFormFirstname', 'name': "firstname", 'class': 'form-control',  'placeholder': 'First name'
    })))
    last_name = forms.CharField(max_length=55, required=False, widget=(forms.TextInput(attrs={
        'id': 'contactFormLastname', 'name': "lastname", 'class': 'form-control', 'placeholder': 'Last name'
    })))
    subject = forms.CharField(max_length=155, required=False, widget=(forms.TextInput(attrs={
        'id': 'contactFormSubject', 'name': "subject", 'class': 'form-control', 'placeholder': 'Subject'
    })))
    email = forms.CharField(max_length=255, required=False, widget=(forms.TextInput(attrs={
        'id': 'contactFormEmail', 'name': "email", 'class': 'form-control', 'type': 'email', 'placeholder': 'Email Address'
    })))
    message = forms.CharField(required=False, widget=(forms.Textarea(attrs={
        'id': 'contactFormMessage', 'name': "message", 'class': "form-control", 'placeholder': "Write your message."
    })))

    class Meta:
        model = contactModel
        fields = '__all__'
