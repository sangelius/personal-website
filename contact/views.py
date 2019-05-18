import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail

from website.settings import DEFAULT_FROM_EMAIL

from .models import Contacts
from .forms import ContactForm

# saves a copy of contact information to database and sends email with that information
def submit_contact(request):
    data = {}
    if request.method == 'POST':
        if request.is_ajax():
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
                context = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'message': message,
                }
                email = render_to_string('contact/email_template.html', context)
                send_mail(
                    subject,
                    email,
                    DEFAULT_FROM_EMAIL,
                    [DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )

                data['success'] = 'Your message has been delivered.'
                data['stat'] = 'ok'
            else: #form not valid
                data['error_info'] = 'Please complete form.'
                data['errors'] = dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])
                data['stat'] = 'error'
        else: #not submitted with ajax
            data['error_info'] = 'Not submitted properly'
            data['stat'] = 'error'
    else: #not post
        data['error_info'] = 'Not post'
        data['stat'] = 'error'

    #send json back to page
    return HttpResponse(json.dumps(data), content_type='application/json')