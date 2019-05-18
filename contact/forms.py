from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, EmailValidator

email_address = EmailValidator(message=_('Invalid entry. Enter a valid email address.'))
phone_num = RegexValidator(r'^[0-9()\- ]*$',
                       message=_('Invalid entry. Enter a valid phone number.'),)

#contact form
class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ContactForm, self).__init__(*args, **kwargs)

    #case name
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Name *',
            'maxlength':'50'
        })
    )

    #email
    email = forms.CharField(
        validators=[email_address],
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Email *',
            'maxlength':'100'
        })
    )

    #phone number
    phone = forms.CharField(
        validators=[phone_num],
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Phone *',
            'maxlength':'14'
        })
    )

    #message
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Message *',
            'maxlength':'2000'
        })
    )
