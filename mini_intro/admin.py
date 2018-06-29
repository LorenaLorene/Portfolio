from __future__ import unicode_literals

from django.contrib import admin

from .models import MiniIntro



class MiniIntroAdmin(admin.ModelAdmin):
    model = MiniIntro
    list_display = ['first_name', 'last_name', 'profession' ]


admin.site.register(MiniIntro, MiniIntroAdmin)
