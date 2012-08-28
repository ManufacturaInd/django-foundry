from django.db import models
from django.utils.translation import ugettext_lazy as _

class Person(models.Model):
    name = models.CharField(_('name'), max_length=120)
    bio = models.TextField(_('short bio'), max_length=10000)
    url1 = models.URLField(_('website 1'), blank=True)
    url2 = models.URLField(_('website 2'), blank=True)
    url3 = models.URLField(_('website 3'), blank=True)
    image = models.ImageField(_('photo'), upload_to='uploads/user_photos')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

class Font(models.Model):
    name = models.CharField(_('name'), max_length=120)
    # Translators: This can mean things like Bold or Italic, as well as other more obscure style names. Note this is different from 'weight'.
    style = models.CharField(verbose_name=_('style'), max_length=120)
    authors = models.ManyToManyField(Person, verbose_name=_('authors'))
    zipfile = models.FileField(verbose_name=_('font file'), upload_to='uploads/fonts')
    # Translators: This is a quick, twitter-like slogan to be displayed as a caption to the font.
    tagline = models.CharField(verbose_name=_('tagline'), max_length=120)
    # Translators: This is a longer description of the font.
    description = models.TextField(verbose_name=_('description'), max_length=10000)
    upload_time = models.DateTimeField(verbose_name=_('upload time'), blank=True, null=True, editable=False)
    last_modified = models.DateTimeField(verbose_name=_('last modified'), blank=True, null=True, editable=False)

    def __unicode__(self):
        return self.name + ' ' + self.style

    class Meta:
        verbose_name = _('font')
        verbose_name_plural = _('fonts')

class FontImage(models.Model):
    font = models.ForeignKey(Font, verbose_name=_('font'), related_name='images')
    image = models.ImageField(verbose_name=_('image'), upload_to='uploads/fontimages')

    def __unicode__(self):
        return self.image.url
    
    class Meta:
        verbose_name = _('font image')
        verbose_name_plural = _('font images')

class Family(models.Model):
    name = models.CharField(_('name'), max_length=120)

    class Meta:
        verbose_name = _('font family')
        verbose_name_plural = _('font families')
