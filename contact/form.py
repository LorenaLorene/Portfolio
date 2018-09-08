from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Name', max_length=100)
    contact_email = forms.CharField(label='Email', max_length=200)
    contact_message = forms.CharField(label='Message', max_length=800)
