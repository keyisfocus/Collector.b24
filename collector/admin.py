from django.contrib import admin

from collector.models import Company, Contact, Deal, Lead


@admin.register(Company, Contact, Deal, Lead)
class DataAdmin(admin.ModelAdmin):
    pass
