# -*- coding: utf-8 -*-
from django.shortcuts import render

from contact.forms import ContactForm
from experience.models import Experience
from skills.models import Skills

def index(request):
    content = {}
    return render(request, 'mainsite/index.html', content)

def resume(request):
    content = {
        'experience': Experience.objects.all(),
        'data_skill': Skills.data_skill.all(),
        'backend_skill': Skills.backend_skill.all(),
        'design_skill': Skills.design_skill.all(),
        'frontend_skill': Skills.frontend_skill.all(),
        'contact_form': ContactForm(),
    }
    return render(request, 'mainsite/resume.html', content)

def swing_dance(request):
    content = {
        'contact_form': ContactForm(),
    }
    return render(request, 'mainsite/swing_dance.html', content)
