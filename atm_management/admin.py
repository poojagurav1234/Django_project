from django.contrib import admin
from .models import ATMSite, State, City

# Register your models here.

@admin.register(ATMSite)
class ATMSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_id', 'address', 'state', 'city')
    search_fields = ('name', 'site_id')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state__name')
