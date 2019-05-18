from django.db import models
from django.utils.translation import gettext as _

class Experience(models.Model):
    '''
    Job experience
    '''

    #job title
    job_title = models.CharField(
        verbose_name=_('Job Title'),
        max_length=100,
        blank=False
    )

    #employer
    employer = models.CharField(
        verbose_name=_('Employer'),
        max_length=100,
        blank=False
    )

    #start date
    start_date = models.CharField(
        verbose_name=_('Start Date'),
        max_length=100,
        blank=False
    )

    #end date
    end_date = models.CharField(
        verbose_name=_('End Date'),
        max_length=100,
        blank=False
    )

    #description
    description = models.TextField(
        verbose_name=_('Description'),
        blank=False
    )

    #order
    order = models.SmallIntegerField(
        verbose_name=_('Order on website'),
        blank=False
    )

    #dates
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Job Experience"
        ordering = ['order']

    def __str__(self):
        return self.job_title
