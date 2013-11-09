from django.contrib import admin
from highlight import models

class ModelAdmin(admin.ModelAdmin):
  list_filter = ['created']
  search_fields = ['text']

admin.site.register(models.Moment, ModelAdmin)
