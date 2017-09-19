from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
    list_lisplay = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_Fields = ('verb',)

admin.site.register(Action, ActionAdmin)
