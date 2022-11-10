import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import JsonResponse

from website.settings import DEFAULT_FROM_EMAIL

from .models import Contacts
from .forms import ContactForm

# saves a copy of contact information to database and sends email with that information
def submit_contact(request):
    data = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            message=form.cleaned_data.get('message')

            # create database entry of contact information
            contact = Contacts.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            contact.save()

            # send email with information
            subject = 'New contact from personal website: %s' % name
            email_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
            }
            email_text = render_to_string('contact/email_template.html', email_data)
            send_mail(
                subject,
                email_text,
                DEFAULT_FROM_EMAIL,
                ['scottangelius@gmail.com'],
                fail_silently=False
            )

            data['success'] = 'Your message has been delivered.'
            data['stat'] = 'ok'
        else: #form not valid
            data['error_info'] = 'Please complete form.'
            data['errors'] = form.errors.as_json()
            data['stat'] = 'error'
    else: #not post
        data['error_info'] = 'Not post'
        data['stat'] = 'error'

    #send json back to page
    return JsonResponse(data)
