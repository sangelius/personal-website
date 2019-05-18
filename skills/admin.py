from django.contrib import admin

from .models import Skills

class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        'skill',
        'category',
        'order',
        'created_date',
        'modified_date'
    )
    ordering = (
        'category',
        'order'
    )

admin.site.register(Skills, SkillsAdmin)
