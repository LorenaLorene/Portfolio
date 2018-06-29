from __future__ import unicode_literals

from django.contrib import admin

from .models import About



class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ['page_name', 'description', 'image']


admin.site.register(About, AboutAdmin)
