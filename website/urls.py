from django.conf.urls import url
from django.contrib import admin

from mainsite.views import *
from contact.views import submit_contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^swing-dancing/$', swing_dance, name='swing_dance'),
    url(r'^submit-contact/$', submit_contact, name='submit_contact'),
    url(r'^admin/', admin.site.urls),
]
