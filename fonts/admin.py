from django.contrib import admin
from models import FontImage, Font, Person

class FontImageInline(admin.TabularInline):
    model = FontImage
    extra = 5

class FontAdmin(admin.ModelAdmin):
    inlines = [ FontImageInline, ]
class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Font, FontAdmin)
