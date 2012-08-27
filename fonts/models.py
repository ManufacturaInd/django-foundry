from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(max_length=10000)
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)
    image = models.ImageField(upload_to='uploads/user_photos')

class Font(models.Model):
    name = models.CharField(max_length=120)
    style = models.CharField(max_length=120)
    authors = models.ManyToManyField(Person)
    zipfile = models.FileField('ZIP file', upload_to='uploads/fonts')
    tagline = models.CharField(max_length=120)
    description = models.TextField(max_length=10000)
    upload_time = models.DateTimeField(blank=True, editable=False)
    last_modified = models.DateTimeField(blank=True, editable=False)

class FontImage(models.Model):
    font = models.ForeignKey(Font, related_name='images')
    image = models.ImageField(upload_to='uploads_fontimages')

class Family(models.Model):
    name = models.CharField(max_length=120)
