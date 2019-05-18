from django.contrib import admin

from .models import Projects, Techs

class TechsInline(admin.TabularInline):
    model = Techs

class ProjectsAdmin(admin.ModelAdmin):
    inlines = (TechsInline,)
    list_display = (
        'name',
        'website',
        'highlight',
        'highlight_order',
        'created_date',
        'modified_date'
    )
    ordering = (
        '-modified_date',
    )

admin.site.register(Projects, ProjectsAdmin)
