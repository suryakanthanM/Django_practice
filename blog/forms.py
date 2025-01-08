from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nmae', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(lable='Message', widget=forms.Textarea)