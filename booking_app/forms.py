from django import forms
from .models import bookingSpace

class bookingForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'sheduleFormFullname', 'class': 'form-control', 'placeholder': "Full name", 'required': ''}))
    busStop = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'sheduleFormBusStop', 'class': 'form-control', 'placeholder': "Bus Stop", 'required': ''}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'sheduleFormAddress', 'class': 'form-control', 'placeholder': "Address", 'aria-label': "Username", 'aria-describedby': "basic-addon1", 'required': ''}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'sheduleFormDescription', 'class': 'form-control', 'placeholder': "Description e.g cotton, wool", 'aria-label': "Username", 'aria-describedby': "basic-addon1", 'required': ''}))
    message = forms.CharField(label=False, required=False, widget=forms.Textarea(
        attrs={'id': 'sheduleFormMessage', 'class': 'form-control', 'placeholder': "Additional Message - i.e. something that can help us serve you better.", 'cols': "30", 'rows': "10"}))
    
    class Meta:
        model = bookingSpace
        fields = ('fullname', 'busStop', 'address',
                  'description', 'message',)







