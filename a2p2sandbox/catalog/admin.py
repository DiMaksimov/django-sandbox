from django.contrib import admin

from .models import CatalogItem


# Register your models here.
class CatalogItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_timestamp', 'updated_timestamp', )
    fieldsets = [
        ('General info',    {'fields': ['title', 'description']}),
        ('Timestamps',      {'fields': ['created_timestamp', 'updated_timestamp']}),
        (None,              {'fields': ['item_image']})
    ]
    list_display = ('title', 'created_timestamp', 'updated_timestamp')
    list_filter = ['created_timestamp']
    search_fields = ['title', 'description']


admin.site.register(CatalogItem, CatalogItemAdmin)
