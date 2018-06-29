from __future__ import unicode_literals

from django.contrib import admin

from .models import Intro



class IntroAdmin(admin.ModelAdmin):
    model = Intro
    list_display = ['page_name', 'introduction', 'description', 'scroll_button']


admin.site.register(Intro, IntroAdmin)
