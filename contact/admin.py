from django.contrib import admin

from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'created_date',
        'message'
    )
    ordering = (
        '-created_date',
    )

admin.site.register(Contacts, ContactsAdmin)
