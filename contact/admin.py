from __future__ import unicode_literals

from django.contrib import admin

from .models import ContactPage



class ContactAdmin(admin.ModelAdmin):
    model = ContactPage
    list_display = ['page_name', 'contact_description' ]


admin.site.register(ContactPage, ContactAdmin)
