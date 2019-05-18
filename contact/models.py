from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import EmailValidator

email_address = EmailValidator(message=_('Invalid entry. Enter a valid email address.'))

class Contacts(models.Model):
    '''
    Information of people that have used the contact form.
    '''

    #name
    name = models.CharField(
        verbose_name=_('Contact Name'),
        max_length=50,
        blank=False
    )

    #email
    email = models.CharField(
        verbose_name=_('Email'),
        max_length=100,
        blank=False,
        validators=[email_address]
    )

    #phone
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=14,
        blank=False
    )

    #message
    message = models.TextField(
        verbose_name=_('Message'),
        max_length=2000,
        blank=False
    )

    #date
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name
