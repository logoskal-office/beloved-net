from django.contrib import admin

from .models import *

class SeriesPartInline(admin.TabularInline):
    model = SeriesPart
    extra = 0
    fields = ['position', 'teaching', 'series']


class TeachingAdmin(admin.ModelAdmin):
    inlines = []
    
class SeriesAdmin(admin.ModelAdmin):
    inlines = [SeriesPartInline]
    



admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(SeriesPart)

