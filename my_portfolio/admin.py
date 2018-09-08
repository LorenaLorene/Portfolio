from django.contrib import admin
from .models import Portfolio
from .models import Project


class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    list_display = ['name', 'description_field']


admin.site.register(Portfolio, PortfolioAdmin)


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['project_name', 'project_link']


admin.site.register(Project, ProjectAdmin)

