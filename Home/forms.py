from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="", max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email_address = forms.EmailField(label="", max_length=150,
                                     widget=forms.EmailInput(attrs={'placeholder': 'John.doe@example.com'}))
    phone_number = forms.RegexField(label="", regex=r'^\+?1?\d{9,15}$',
                                    error_messages=({'invalid': "Phone number must be entered in the format: "
                                                                "'+999999999'. Up to 15 digits allowed."}),
                                    widget=forms.TextInput(attrs={'placeholder': '+971526698242'}))
    message = forms.CharField(label="",
                              widget=forms.Textarea(attrs={
                                  'cols': 15, 'rows': 5, 'placeholder': 'Enter your message here...'}), max_length=2000)
