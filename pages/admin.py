import imp
from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
    thumbnail.short_description="photo"
    list_display=('id','thumbnail','first_name','designation','created_date') #this is for make show clickable in admin panel
    list_display_links=('first_name','thumbnail','id') #this is for make fielsd clickable in admin panel
    search_fields=('first_name','last_name','designation') #this is search field,django gives
    list_filter=('designation',) #this is filter area by django
admin.site.register(Team,TeamAdmin)