from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import URLValidator

webaddress = URLValidator()

class HighlightManager(models.Manager):
    '''
    Selects only projects that are highlights
    '''
    def get_queryset(self):
        return super(HighlightManager, self).get_queryset().filter(highlight=True)

class Projects(models.Model):
    '''
    Portfolio projects for display on main page and subsequent pages
    '''

    #project or website name
    name = models.CharField(
        verbose_name=_('Project Name'),
        max_length=100,
        blank=False
    )

    #project's website
    website = models.CharField(
        verbose_name=_('Project Website'),
        max_length=200,
        blank=False,
        validators=[webaddress]
    )

    #project's image location
    img_location = models.CharField(
        verbose_name=_('Project Image Location'),
        max_length=200,
        blank=False
    )

    #project's short description
    short_description = models.TextField(
        verbose_name=_('Project Short Description'),
        max_length=2000,
        blank=False
    )

    #project's long description
    long_description = models.TextField(
        verbose_name=_('Project Long Description'),
        blank=False
    )

    #highlighted project
    highlight = models.BooleanField(
        verbose_name=_('Highlight'),
        default=False
    )

    #highlight order
    highlight_order = models.SmallIntegerField(
        verbose_name=_('Order on highlights'),
        blank=False
    )

    #dates
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    #managers
    objects = models.Manager()
    highlighted = HighlightManager()

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['-modified_date']

    def __str__(self):
        return self.name

class Techs(models.Model):
    '''
    Technologies utilized in project
    '''

    #project
    project = models.ForeignKey(
        Projects,
        related_name='project_tech',
        blank=False
    )

    #tech type
    tech_type = models.CharField(
        verbose_name=_('Technology Used'),
        max_length=50,
        blank=False
    )

    class Meta:
        verbose_name_plural = "Techs"
