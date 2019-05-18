from django.db import models
from django.utils.translation import gettext as _

class DesignSkillManager(models.Manager):
    '''
    Selects only skills that are category 'design'
    '''
    def get_queryset(self):
        return super(DesignSkillManager, self).get_queryset().filter(category=1).order_by('order')

class BackendSkillManager(models.Manager):
    '''
    Selects only skills that are category 'back-end'
    '''
    def get_queryset(self):
        return super(BackendSkillManager, self).get_queryset().filter(category=2).order_by('order')

class FrontendSkillManager(models.Manager):
    '''
    Selects only skills that are category 'front-end'
    '''
    def get_queryset(self):
        return super(FrontendSkillManager, self).get_queryset().filter(category=3).order_by('order')

class DataSkillManager(models.Manager):
    '''
    Selects only skills that are category 'data analysis'
    '''
    def get_queryset(self):
        return super(DataSkillManager, self).get_queryset().filter(category=4).order_by('order')

class Skills(models.Model):
    '''
    Skills as a designer and developer
    '''

    #category of skill
    category_choices = [
        (1, 'Design'),
        (2, 'Back-end'),
        (3, 'Front-end'),
        (4, 'Data analysis'),
    ]
    category = models.IntegerField(
        verbose_name=_('Category'),
        choices=category_choices,
        blank=False
    )

    #skill
    skill = models.CharField(
        verbose_name=_('Skill'),
        max_length=100,
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

    #managers
    objects = models.Manager()
    design_skill = DesignSkillManager()
    backend_skill = BackendSkillManager()
    frontend_skill = FrontendSkillManager()
    data_skill = DataSkillManager()

    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['-modified_date']

    def __str__(self):
        return self.skill

    def get_category(self):
        try:
            text = dict(Skills.category_choices)[self.category]
        except KeyError:
            text = ''
        return text
