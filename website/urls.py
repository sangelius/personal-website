from django.urls import re_path
from django.contrib import admin

from mainsite.views import *
from contact.views import submit_contact

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^swing-dancing/$', swing_dance, name='swing_dance'),
    re_path(r'^resume/$', resume, name='resume'),
    re_path(r'^submit-contact/$', submit_contact, name='submit_contact'),
    re_path(r'^admin/', admin.site.urls),
]
