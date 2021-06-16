from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    full_name = forms.CharField(label="", max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email_address = forms.EmailField(label="", max_length=150,
                                     widget=forms.EmailInput(attrs={'placeholder': 'John.doe@example.com'}))
    phone_number = PhoneNumberField(label="", widget=forms.TextInput(attrs={'placeholder': '+971526698242'}))
    message = forms.CharField(label="",
                              widget=forms.Textarea(attrs={
                                  'cols': 15, 'rows': 5, 'placeholder': 'Enter your message here...'}), max_length=2000)
