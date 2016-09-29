from django.contrib import admin

from .models import *

class CountHeaderAdmin(admin.ModelAdmin):
    list_display = ('count_date', 'description')
    
admin.site.register(CountHeader,CountHeaderAdmin)
admin.site.register(CountLines)
