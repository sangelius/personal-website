from django.contrib import admin

from .models import Experience

class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'employer',
        'start_date',
        'end_date',
        'description',
        'order',
        'created_date',
        'modified_date'
    )
    ordering = (
        'order',
    )

admin.site.register(Experience, ExperienceAdmin)
